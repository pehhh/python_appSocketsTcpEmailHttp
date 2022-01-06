import socket, os

HOST = '127.0.0.1'

PORT = 65432
msg = ''
name = ''
opcion = ''
dataChat = ''
sugerencia = ''
email = ''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))
    c.send('cliente conectado'.encode('utf-8'))
    data = c.recv(1024).decode('utf-8')
    while True:
        data = c.recv(1024).decode('utf-8')
        if ('nombre' in data):
            name = input(data)
            c.send(name.encode('utf-8'))
        elif ('opcion' in data):
            print('opicion'+data)
            opcion = input('opcion: ')
            c.send(opcion.encode('utf-8'))
        elif('server' in data):
            print('estoy en el chat')
            print(data)
            while True:
                msg = input(name+'>')
                msg = name+'>'+msg
                c.send(msg.encode('utf-8'))
                if('exit' in msg):
                    break
                dataChat = c.recv(1024).decode('utf-8')
                print(dataChat)
                if('exit' in dataChat):
                    break
        elif('chat' in data):
            print(data)
            while True:
                dataChat = c.recv(1024).decode('utf-8')
                print(dataChat)
                if('exit' in dataChat):
                    break
                msg = input(name+'>')
                msg = name+'>'+msg
                c.send(msg.encode('utf-8'))
                if('exit' in msg):
                    break
        elif('email' in data):
            while True:
                email2 = input(data)
                c.send(email2.encode('utf-8'))
                dataSug=c.recv(1024).decode('utf-8')
                sugerencia=input(dataSug)
                c.send(sugerencia.encode('utf-8'))
                if(email2!='' and sugerencia!=''):
                    break
        elif('archivo' in data):
            emailArchivo=input(data)
            c.send(emailArchivo.encode('utf-8'))
            dataArchivo=c.recv(1024).decode('utf-8')
            while True:
                emailArchivo=input(data)
                c.send(emailArchivo.encode('utf-8'))
                dataArchivo=c.recv(1024).decode('utf-8')
                archivo = input(dataArchivo)
                if os.path.exists(archivo):
                    c.send(archivo.encode('utf-8'))
                    print('archivo enviado')
                    break
                else:
                    print('archivo no encontrado, prueba de nuevo')
        elif ('vista' in data):
            print(data)
            break        
                               