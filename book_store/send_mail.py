import smtplib
from email.message import EmailMessage

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "mohammadsadeghsherbaf@gmail.com"
EMAIL_HOST_PORT = 465 
EMAIL_HOST_PASSWORD = "qvhszprjfmbinmrd"


msg = EmailMessage()

msg['Subject'] = "Python sender created by Sadegh"
msg['From'] = EMAIL_HOST_USER
msg['To'] = ""
msg.set_content("Hi babe this is a test mail sended automaticly by python. from TASEKH :) I LOVE YOU soooo muchhh")
 
with smtplib.SMTP_SSL(EMAIL_HOST,EMAIL_HOST_PORT) as server:
    server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    server.send_message(msg)








































#"negin.a.hosseini82@gmail.com"