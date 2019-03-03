from flask_mail import Message
from app import mail,app
from flask import render_template
from threading import Thread

def send_email(subject, sender, recepients,text_body, html_body):
    msg=Message(subject, sender=sender, recepients=recepients)
    msg.body=text_body
    msg.html=html_body
    mail.send(msg)
    Thread(target=send_async_email, args=(app,msg)).start()

def send_password_reset_email(user):
    token=user.get_reset_password_token()
    send_email('[Microblog: reset your email]',sender=app.config[ADMINS][0],recepients=[user.email], text_body=render_template('email/reset_password.txt', user=user, token=token), html_body=render_template('email/reset_password.html', user=user, token=token))    

def send_async_email(msg, app):
    with app.app_context():
        mail.send(msg)

v    