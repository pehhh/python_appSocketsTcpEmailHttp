import smtplib, ssl

def email(nombre, email,sugerencia,masivo=False):
    i=0
    
    port=465

    password='1_2_3_4_5_6_'

    sender_email=email
    receiver_email=email
    server_domain = "smtp.gmail.com"

    msg='''Subject: Copia de la tu sugerencia

    
    Hola {},gracias por tu sugerencia, te envio una copia:\n {}'''.format(nombre,sugerencia)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(server_domain,port,context=context) as s:
        s.login(sender_email,password)
        if (masivo==False):
            s.sendmail(sender_email,receiver_email,msg)
        else:
            while(i<10):
                s.sendmail(sender_email,receiver_email,msg)
                i+=1

