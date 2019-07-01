import socket
import sys

s = socket.socket()

port = 12121

s.connect(('127.0.0.1',port))

try:
    f = open("data_recieved.txt","w")
    f.write(s.recv(1024))
    f.close()

    s.close()

    s = socket.socket()
    print "Socket created successfully!"

    port = 12122

    s.bind(('',port))
    print "Socket bind to " + str(port)

    s.listen(5)
    print "Socket is listening"

    while True:
        connection, address = s.accept()
        print "Got connection from " + str(address)
        f = open("data_recieved.txt","r")
        connection.send(f.read())
        connection.close()
except Exception as err:
    print "Error : " + err