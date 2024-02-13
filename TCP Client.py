#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

host = '192.168.227.20'
host = socket.gethostname()

port = 444

clientsocket.connect(('192.168.227.20', port))   # Connect to the server on localhost:444

message = clientsocket.recv(1024)     # Receive the message from the server
clientsocket.close()

print(message.decode('ascii'))
