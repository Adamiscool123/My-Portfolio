import os
import smtplib, ssl
from dotenv import load_dotenv

load_dotenv()
def send_email(message, email):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv("PASSWORD")
    receiver = 'adamidrissi177@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(receiver, password)
        server.sendmail(email, receiver, message)

