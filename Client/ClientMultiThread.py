import socket

# Multi thread client using TCP 

print("\nSTARTING MULTITHREAD CLIENT\n")
print("Welcome to John's test client, you are in the client side")
print("\n-------------------------\n")

# Setting the address that the client will connect
HOST_AND_PORT = ("localhost", 21000)

def serverResponses(serverResponse):
    print("\n-------------------------\n")
    print("Server returned as response:", serverResponse.decode() + '\n')
    return
# Creating the socket for the client with its types of connection
while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(HOST_AND_PORT) # Connecting to the tuple with the server's address

    textToSend = input("Type the command: ")
    clientSocket.sendall(str.encode(textToSend))
    serverResponse = clientSocket.recv(4096)
    serverResponses(serverResponse)

    if serverResponse.decode() == '100 # SHUTTING DOWN THE CONNECTION': # make an array of possible commands just to simplify
        print("\n-------------------------\n")
        break

    contentToSend = input("Type the text you want to send: ")
    clientSocket.sendall(str.encode(contentToSend))
    serverResponse2 = clientSocket.recv(2048)
    serverResponses(serverResponse2)

    
