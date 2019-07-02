import socket
import sys
import psutil

count = 0
s = socket.socket()

print "Trying to connect to any open server ..."


pids = psutil.pids()
for p in pids:
    a = psutil.Process(p)
    if(a.name() == "python"):
        if len(a.connections()) == 0:
            count += 1
        else:
            break
    else:
        count += 1
        if (count == len(pids)):
            print "No active server available"
            sys.exit()

port = a.connections()[0][3][1]
try:
    s.connect(('127.0.0.1',port))
    print "Server found at port : " + str(port)
except Exception as err:
    print "Error : " + str(err)
    sys.exit()
    
try:
    f = open("data_recieved.txt","w")
    f.write(s.recv(1024))
    f.close()

    s.close()

    s = socket.socket()
    print "Socket created successfully!"

    port = port + 1

    s.bind(('',port))
    print "Socket bind to " + str(port)

    s.listen(5)
    print "Socket is listening"

    while True:
        try:
            connection, address = s.accept()
            print "Got connection from " + str(address)
            f = open("data_recieved.txt","r")
            connection.send(f.read())
            connection.close()
        except Exception as err:
            print "Can't connect to client. Trying again ..."
except Exception as err:
    print "Error : " + str(err)
    sys.exit()
        