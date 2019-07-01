import socket
import sys

s = socket.socket()

print "You currently have 2 seeds. Which one you want to access?"
print "\n 1 : 12121 \n 2 : 12122"
choice = int(raw_input("Enter your choice (1/2) : "))
if choice == 1:
    port = 12121
    try:
        s.connect(('127.0.0.1',port))
    except Exception as err:
        print "12121 is not available, pivoting to 12122 ..."
        port = 12122
        s.connect(('127.0.0.1',port))
else:
    port = 12122
    try:
        s.connect(('127.0.0.1',port))
    except Exception as err:
        print "12122 is not available, pivoting to 12121 ..."
        port = 12121
        s.connect(('127.0.0.1',port))

f = open("data3.txt","w")
f.write(s.recv(1024))
f.close()
s.close()