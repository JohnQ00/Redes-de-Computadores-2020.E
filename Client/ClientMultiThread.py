import socket

# Multi thread client using TCP 

print("\nSTARTING MULTITHREAD CLIENT\n")
print("Welcome to John and Hiago's test client, you are in the client side")
print("\n-------------------------\n")

commandsDictionary = ["100 # SHUTTING DOWN THE CONNECTION"]
# Setting the address that the client will connect
HOST_AND_PORT = ("localhost", 22000)

# Creating the socket for the client with its types of connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(HOST_AND_PORT) # Connecting to the tuple with the server's address

def serverResponses(serverResponse):
    print("\n-------------------------\n")
    print("Server returned as response:", serverResponse.decode() + '\n')
    return

while True:
    textToSend = input("Type the command: ")
    clientSocket.sendall(str.encode(textToSend))
    serverResponse = clientSocket.recv(4096)
    serverResponses(serverResponse)

    if serverResponse.decode() == commandsDictionary[0]: # make an array of possible commands just to simplify
        print("-------------------------\n")
        break

    contentToSend = input("Type the text you want to send: ")
    clientSocket.sendall(str.encode(contentToSend))
    serverResponse = clientSocket.recv(4096)
    serverResponses(serverResponse)

    
