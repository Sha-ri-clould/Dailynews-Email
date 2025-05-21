import smtplib , ssl
import os
from email.message import EmailMessage

def send_email(body):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("SENDER_MAIL")
    password = os.getenv("MAIL_PASSWORD")

    receiver= os.getenv("RECEIVER_MAIL")
    context = ssl.create_default_context()

    if isinstance(body, bytes):
        body = body.decode('utf-8')

    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = "Today's news articles"
    msg.set_content(body)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)
        print("Email sent")
