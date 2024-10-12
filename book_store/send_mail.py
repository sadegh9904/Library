import smtplib
from email.message import EmailMessage

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "mohammadsadeghsherbaf@gmail.com"
EMAIL_HOST_PORT = 465 
EMAIL_HOST_PASSWORD = "qvhszprjfmbinmrd"


msg = EmailMessage()

msg['Subject'] = "Warning"
msg['From'] = EMAIL_HOST_USER
msg['To'] = ""
msg.set_content("your deadline is over!")
 
with smtplib.SMTP_SSL(EMAIL_HOST,EMAIL_HOST_PORT) as server:
    server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    server.send_message(msg)