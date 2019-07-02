import socket
import sys
import random

s = socket.socket()
print "Socket created successfully!"

port = random.randint(1024,65535)

s.bind(('',port))
print "Socket bind to " + str(port)

s.listen(5)
print "Socket is listening"

while True:
    try:
        connection, address = s.accept()
        print "Got connection from " + str(address)
        f = open("data_send.txt","w+")
        f.write("Hey, guys! I do have the file.")
        f.close()
        f = open("data_send.txt","r")
        connection.send(f.read())
        connection.close()
    except Exception as err:
        print "Can't connect to client. Trying Again ..."