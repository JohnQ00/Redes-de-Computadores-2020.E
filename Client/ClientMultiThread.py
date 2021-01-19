import socket
from Client import ClientTextProvider

# Multi thread client using TCP 
 
ClientTextProvider.client_introduction("CLIENT")

class WrongCommand(Exception):
    pass

commandsDictionary = ["100 # SHUTTING DOWN THE CONNECTION"]
# Setting the address that the client will connect
HOST_AND_PORT = ("localhost", 15000)

# Creating the socket for the client with its types of connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(HOST_AND_PORT) # Connecting to the tuple with the server's address

def serverResponses(serverResponse):
    print("\n-------------------------\n")
    print("Server returned as response:", serverResponse.decode() + '\n')
    return

def commandInput():
    while True:
        try:
            textToSend = input("Type the command: ")
            if textToSend != "UPPER" and textToSend != "DISCONNECT":
                raise WrongCommand
            break
        except WrongCommand:
            print("\nYou mistyped the command. Please, try again\n")
    return textToSend
            
while True:
    textToSend = commandInput()
    
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

    
