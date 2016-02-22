#!/usr/bin/python

"""
Sumador Simple
"""

import socket
# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1235))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)
num = None;
suma = None;
try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        peticion = recvSocket.recv(2048)
        print peticion
        if(num == None):
            num = int(peticion.split(' ')[1][1:])
            print "numero recibido" + str(num)
        elif (num != None):
            num2 = int(peticion.split(' ')[1][1:])
            print "numero recibido" + str(num2)
            suma = num + num2

        print 'Answering back...'

        html += "<html><body><h1>Hello World!</h1>"
        html += "<p>And in particular hello to you, "
        html += str(address[0])
        html += "</p>"
        html += "<p>"+ str(suma) + "</p>"
        html += "</body></html>"

        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + html + "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
