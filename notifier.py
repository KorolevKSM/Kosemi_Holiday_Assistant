import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.mail.ru')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
SENDER = os.getenv('MAIL_USER')
PASSWORD = os.getenv('MAIL_PASSWORD')

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER, PASSWORD)
        server.send_message(msg)
    print(f"Письмо отправлено на {to_email}")