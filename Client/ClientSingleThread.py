import socket

# Single thread client using TCP 

print("\nSTARTING SINGLE THREAD CLIENT\n")
print("Welcome to John's test server, you are in the client side")
print("\n-------------------------\n")

# Setting the address that the client will connect
HOST_AND_PORT = ('localhost', 20000)

# Creating the socket for the client with its types of connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(HOST_AND_PORT) # Connecting to the tuple with the server's address
textToSend = input("Type the message you want to send: ")
clientSocket.sendall(str.encode(textToSend))
dataToSend = clientSocket.recv(1024) # Setting the size of the data that will be sent

print("\nMessage succesfully echoed: \n", dataToSend.decode()) 
# The datastream of the message is given in BYTES, so it's necessary to decode the datastream to 'string' again


