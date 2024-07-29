import smtplib
import ssl
from email.message import EmailMessage

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

username = "aashritha1407@gmail.com"
password = "scpy qexg gaev ntjf"


def send_email(username, subject, message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
        server.login(username, password)

        # Construct email
        msg = EmailMessage()
        msg['From'] = username
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.set_content(message)

        server.send_message(msg)
        server.quit()


subject = "Test Mail"

receiver = "aashritha1407@gmail.com"

message = """
Hello!
Test email
Bye!
"""
send_email(username, subject, message)
