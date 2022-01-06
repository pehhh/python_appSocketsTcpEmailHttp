import socket
def httpMarcha():
    HOST='127.0.0.1'
    PORT=8888

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s2:
        s2.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s2.bind((HOST,PORT))
        s2.listen()
        while True:
            print('esperando peticiones')
            conn3, addr3 = s2.accept()
            
            with conn3:
                print('conectado con {}'.format(addr3))
                data=conn3.recv(1024).decode('utf-8')
                peticionSep=data.split(' ')
                metodo=peticionSep[0]
                archivoPeticion=peticionSep[1]
                archivoPeticion=archivoPeticion.lstrip('/')
                print(archivoPeticion)
                if(archivoPeticion == ''):
                    archivoPeticion='./index.html'
                try: 
                    f=open(archivoPeticion,'rb')
                    archivoLeido=f.read()
                    f.close()
                    header='HTTP/1.1 200 OK\n'
                    if(archivoPeticion.endswith('.css')):
                        mimetype='text/css'
                    elif(archivoPeticion.endswith('.jpg')):
                        mimetype='image/jpg'
                    else:
                        mimetype='text/html'
                    header+= 'Content-Type: '+str(mimetype)+'\n\n'
                except Exception as e:
                    header='HTTP/1.1 404 ERROR\n'
                    f=open('./indexError.html','rb')
                    archivoLeido=f.read()
                    f.close()
                peticion=header.encode('utf-8')
                peticion+=archivoLeido
                conn3.send(peticion)
                conn3.close()
                
                #ya que img es el ultimo archivo que pide
                if(archivoPeticion.endswith('.jpg')):
                    break