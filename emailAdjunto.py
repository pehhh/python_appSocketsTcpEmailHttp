import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def envioAdjunto(sender_mail,receiver_mail,nombre,archivo):  
    port = 465
    sender_mail = receiver_mail
    receiver_mail = receiver_mail
    server_domain = "smtp.gmail.com"
    password = '1_2_3_4_5_6_'
    message = MIMEMultipart()

    subject = "Mail con adjunto de : "
    body = "Archivo enviado por {} a traves del servidor".format(nombre)

    message.attach(MIMEText(body, "plain"))

    filename = archivo
    message["Subject"] = subject
    message["From"] = sender_mail
    message["To"] = receiver_mail

    message["Bcc"] = receiver_mail

    with open(filename, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())


    encoders.encode_base64(part)

    part.add_header("Content-Disposition",
                    "atachment;filename={}".format(filename))

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(server_domain
                        , port, context=context) as s:
        s.login(sender_mail, password)
        s.sendmail(sender_mail, receiver_mail, text)
    