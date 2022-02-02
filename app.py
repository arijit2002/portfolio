import pymongo
from flask import Flask,render_template, request,make_response
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("user")
pswd = os.getenv("pswd")
database = os.getenv("database")

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    
    return render_template('index.html')

@app.route('/form',methods=['POST','GET'])
def form():
    myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{pswd}@{database}.gjpbh.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["test"]
    mycol = mydb["portfolio"]
    name=request.form.get('name')
    email=request.form.get('email')
    subject=request.form.get('subject')
    message=request.form.get('message')
    print(name,email,subject,message)
    list={"name":name,"email":email,"subject":subject,"message":message}
    mycol.insert_one(list)
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)