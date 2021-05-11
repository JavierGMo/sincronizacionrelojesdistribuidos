from datetime import datetime
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.bind(('localhost', 3000))
sock.listen(10)
connection, clientAddress = sock.accept()

data = connection.recv(32).decode()
if data:
    print('Recibido en server : {}'.format(data))
    now = datetime.now()


    connection.sendall('{}:{}:{}'.format(now.hour, now.minute, now.second).encode())
else:
    print('No data')

connection.close()