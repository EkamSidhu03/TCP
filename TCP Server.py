#1/urs/bin/python3
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
#host = '192.168.227.20'   # Server IP address
host = socket.gethostname()
port = 444

serversocket.bind( ( '192.168.227.20', port ) )                        # Bind to the port

serversocket.listen(5)                                   # Now wait for client connection.
print("Server is listening on port ", port)               # You can see this message if you run

while  True:                                             # Server will keep running until it's stopped manually or crashes
    clientsocket, address = serversocket.accept()

    print("Got connection from %s " % str(address))              # The string is just an informational message
    
    message = 'Hello! Thank you for  connecting!' + "\r\n"        # Send some initial chat messages
    clientsocket.send(message.encode('ascii'))              # Convert to bytes before sending

    clientsocket.close()                            # Close the connection stream with the client