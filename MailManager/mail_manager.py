import smtplib
import ssl
from email.mime.text import MIMEText


def send_mail(value, change_percent):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_mail = "btcservice@yny.com"
    receiver_mail = "yagizhanyakali@gmail.com"
    username = "***"
    password = "***"
    subject = "Subject: Guncel BTC Degeri Hakkinda"
    body = "BTC guncel degeri: {}TL\nDegisim Yuzdesi: {}".format(value, change_percent)

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_mail
    message['To'] = receiver_mail

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(username, password)
            server.sendmail(sender_mail, receiver_mail, message.as_string())
            print("Mail sent!")
    except Exception as ex:
        print(ex)
