import pymongo
from flask import Flask,render_template, request,make_response
import smtplib
from email.mime.text import MIMEText


app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    
    return render_template('index.html')

@app.route('/form',methods=['POST','GET'])
def form():
    name=request.form.get('name')
    email=request.form.get('email')
    subject=request.form.get('subject')
    message=request.form.get('message')
    
    modified="Email of Sender: "+email+"\n"+message
    
    msg=MIMEText(modified)
    fromAddr="sender_mail"
    toAddr="receiver_mail"
    
    msg['From']=fromAddr
    msg['To']=toAddr
    msg['Subject']=subject

    server=smtplib.SMTP("smtp.gmail.com",587) #587 is the gmail port number 

    #put the smtp connection in TLS mode
    server.starttls()
    server.login(fromAddr, 'pswd') 
    server.send_message(msg)
    print("Mail sent")
    server.quit()
    #close the server before exiting
    
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
