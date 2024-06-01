import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "gianlucaproto@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "gianlucaproto@gmail.com"
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email inviata con successo!")
    except Exception as e:
        print(f"Errore durante l'invio dell'email: {e}")



