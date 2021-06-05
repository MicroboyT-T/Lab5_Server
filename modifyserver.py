import socket
import sys

s = socket.socket()
print("Socket successfully created...")

port = 8888

s.bind(('', port))
print("Socket binded to " + str(port))

s.listen(5)
print("Socket is listening...")

while True:
        c, addr = s.accept()
        print("Got connection from" + str(addr))
        with open('virus.txt', 'wb') as f:
            print('Opening file...')
            print('Receiving file from client...')
            data = c.recv(1024)
            print('Data from file: ', (data))
            if not data:
                break
            f.write(data)
        f.close()
        c.close()
        print('Successfully get the file from client...')
        print('Server is closing the connection...')
        exit()
c.close()
