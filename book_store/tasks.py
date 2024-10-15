from celery import shared_task
from .models import Borrow,Book
from django.utils import timezone
from datetime import timedelta
import smtplib
from email.message import EmailMessage



EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "mohammadsadeghsherbaf@gmail.com"
EMAIL_HOST_PORT = 465 
EMAIL_HOST_PASSWORD = "qvhszprjfmbinmrd"


@shared_task
def check_books():

    ten_days_ago = timezone.now() - timedelta(hours=6)

    borrows = Borrow.objects.filter(
        borrow_date__gte=ten_days_ago, return_date__isnull = True )
    
    for borrow in borrows:
        user_email = borrow.user.email


        
        msg = EmailMessage()

        msg['Subject'] = "Warning"
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = user_email
        msg.set_content(f"Dear {borrow.user.username},your period for the book {borrow.book.title} has expired.")
        
        with smtplib.SMTP_SSL(EMAIL_HOST,EMAIL_HOST_PORT) as server:
            server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
            server.send_message(msg)