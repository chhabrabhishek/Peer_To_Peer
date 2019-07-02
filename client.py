import socket
import sys
import psutil

list_ports = []
s = socket.socket()

pids = psutil.pids()
for p in pids:
    a = psutil.Process(p)
    if(a.name() == "python"):
        if len(a.connections()) == 0:
            pass
        else:
            list_ports.append(a.connections()[0][3][1])

print "You currently have " + str(len(list_ports)) + " seed(s). Which one you want to access?"
for x in range(0,len(list_ports)):
    print str(x+1) + " : " + str(list_ports[x])
choice = int(raw_input("Enter your choice (S.No) : "))
if choice > len(list_ports):
    print "Can't connect to server."
    sys.exit()

port = list_ports[choice-1]
try:
    s.connect(('127.0.0.1',port))
except Exception as err:
    print "Port unavailable, pivoting to another port ..."
    list_ports.remove(port)
    port = list_ports[0]
    s.connect(('127.0.0.1',port))

f = open("data3.txt","w")
f.write(s.recv(1024))
print "You got your data!"
f.close()
s.close()