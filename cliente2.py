import socket

HOST='127.0.0.1'

PORT=65432
msg=''
name=''
opcion=''
dataChat=''
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
    c.connect((HOST,PORT))
    
    while True:
        data=c.recv(1024).decode('utf-8')
        if ('nombre' in data):
            name=input(data)
            c.send(name.encode('utf-8'))
        elif('chat' in data):
            
            print(data)
            while True:
                msg=input(name+'>')
                msg=name+'>'+msg
                c.send(msg.encode('utf-8'))
                if('exit' in msg):
                    break
                dataChat=c.recv(1024).decode('utf-8')
                print(dataChat)
                if('exit' in dataChat ):
                    break
            break