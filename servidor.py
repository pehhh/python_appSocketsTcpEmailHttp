from ctypes import py_object
import socket,csv,smtplib,ssl
import emailEnvio
import httpCliente
import emailAdjunto

HOST='127.0.0.1'

PORT=65432
msg=''
name=''
name2=''
msgOpcion='''
Hola, elige una opcion:
    1. Hablar con el operador del servidor, para salir teclea exit
    2. Chat con amigo (incluir cliente2 en conversacion), para salir cualquiera de los dos debe teclear exit
    3. Enviarnos sugerencia
    4. Enviar correo personalizado con sugerencias guardadas a sus propietarios, con opcion de correo masivo
    5. Subir web para poder acceder desde localhost puerto 8888
    6. Enviar archivo a un email a traves del servidor. Introducir archivo de la misma carpeta, por ejemplo, cliente.py
    7. Salir
'''
opcion=''
msgEnvio=''
i=0
email=''
sugerencia=''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((HOST,PORT))
    s.listen()
    print('esperando peticiones')
    conn,addr=s.accept()
    
    with conn:
        print('conectado con ',addr)
        conn.send('hola, bienvenido a mi servidor'.encode('utf-8'))
        data=conn.recv(1024).decode('utf-8')
        while True:
            if name=='':
                conn.send('en primer lugar dime tu nombre: '.encode('utf-8'))
                name=conn.recv(1024).decode('utf-8')
            else:
                conn.send(msgOpcion.encode('utf-8'))
                opcion=conn.recv(1024).decode('utf-8')
                if opcion =='1':
                    while True:
                        msgEnvio=input('server>')
                        msgEnvio='server>'+msgEnvio
                        conn.send(msgEnvio.encode('utf-8'))
                        if('exit' in msgEnvio ):
                            break
                        data=conn.recv(1024).decode('utf8')
                        print(data)
                        if('exit' in data):
                            break
                elif opcion=='2':  
                    print('esperando a su amigo')
                    conn2,addr2=s.accept()
                    with conn2:
                        conn2.send('hola, dime tu nombre: '.encode('utf-8'))
                        name2=conn2.recv(1024).decode('utf-8')
                        print('el amigo se llama'+name2)
                        msgEnvio='hola , estas en un chat con '+name2
                        conn.send(msgEnvio.encode('utf-8'))
                        msgEnvio2='hola , estas en un chat con '+name
                        conn2.send(msgEnvio2.encode('utf-8'))
                        print('mensajes conexion enviados')
                        while True:
                            data2=conn2.recv(1024).decode('utf-8')
                            conn.send(data2.encode('utf-8'))
                            print(data2)
                            if('exit' in data2):
                                break
                            data=conn.recv(1024).decode('utf-8')
                            conn2.send(data.encode('utf-8'))
                            print(data)
                            if('exit' in data):
                                break
                            data2=''
                            data=''           
                elif opcion =='3':
                    while True:
                        conn.send('dime tu email : '.encode('utf-8'))
                        email=conn.recv(1024).decode('utf-8')
                        conn.send('escribe tu sugerencia : '.encode('utf-8'))
                        sugerencia=conn.recv(1024).decode('utf-8')
                        f=open('sugerencias.csv','a')
                        f.write(email+','+ sugerencia+'\n')
                        f.close()
                        print(email)
                        print(sugerencia)
                        if(email!='' and sugerencia!=''):
                            break
                elif opcion=='4':
                    f=open('sugerencias.csv','r')
                    ficheroArray=f.readlines()
                    f.close()
                    for line in ficheroArray:
                        arr=line.split(',')
                        emailEnvio.email(name,arr[0],arr[1],False)
                        print('correo enviado a {} con email {}'.format(name,arr[0]))
                elif opcion=='5':
                    httpCliente.httpMarcha()
                elif opcion=='6':
                    while True:
                        conn.send('dime el email al que quieres enviar el archivo : '.encode('utf-8'))
                        emailArchivo=conn.recv(1024).decode('utf-8')
                        conn.send('enviame el archivo que quieres enviar : '.encode('utf-8'))
                        archivoRecibido=conn.recv(65536)
                        f=open(archivoRecibido,'r')
                        archivoLeido=f.read()
                        f.close()
                        print('contenido del archivo: ')
                        print(archivoLeido)
                        continuar=input('el contenido del archivo es adecuado, contesta si o no para continuar con el envio :')
                        if (continuar=='si'):
                            #pongo la misma direccion, porque uso siempre la misma para enviar y recibir
                            emailAdjunto.envioAdjunto(emailArchivo,emailArchivo,name,archivoRecibido)
                            print('email enviado')
                            break
                        else:
                            print('no apto para envio')
                            break
                elif opcion=='7':
                    conn.send('hasta la vista'.encode('utf-8'))
                    break       
