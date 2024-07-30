import os
import smtplib
import ssl
from email.message import EmailMessage
import os

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

username = "aashritha1407@gmail.com"
password = os.getenv("PASSWORD")
#password = "scpy qexg gaev ntjf"

receiver = "aashritha1407@gmail.com"


def send_email(message, user_email, subject):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
        server.login(username, password)

        # Construct email
        subject = f"{subject}"
        msg = EmailMessage()
        msg['From'] = user_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.set_content(f"\nFrom: {user_email} \n" + message)

        server.send_message(msg)
        server.quit()



# message = """
# Hello!
# Test email
# Bye!
# """
#send_email(message)
