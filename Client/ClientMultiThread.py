import socket
import ApplicationCommands

# Multi thread client using TCP 

print("\nSTARTING MULTITHREAD CLIENT\n")
print("Welcome to John and Hiago's client, you are in the client side")
print("\n-------------------------\n")

class WrongCommand(Exception):
    pass

# Setting the address that the client will connect
HOST_AND_PORT = ("localhost", 15000)

# Creating the socket for the client with its types of connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(HOST_AND_PORT) # Connecting to the tuple with the server's address

def serverResponses(serverResponse):
    print("\n-------------------------\n")
    print("Server returned as response:", serverResponse.decode())
    print("\n-------------------------\n")
    return

def commandInput():
    while True:
        try:
            textToSend = input("Type the command: ")
            ApplicationCommands.CommandContentHelper(textToSend)
            if bool(not ApplicationCommands.checkCommand(textToSend)):
                raise WrongCommand
            break
        except WrongCommand:
            print("\nYou mistyped the command. Please, try again\n")
    return textToSend
            
while True:
    textToSend = commandInput() 
        
    clientSocket.sendall(str.encode(textToSend))
    serverResponse = clientSocket.recv(4096)
    
    if serverResponse.decode() == ApplicationCommands.commandsCodes[0]:
        serverResponses(serverResponse)
        break

    else:
        serverResponse = serverResponse.decode('utf-8')
        # a = eval(a) TA DANDO ERRO DE EOF
        print("\n-------------------------\n")
        print("Server returned as response:", serverResponse)
        print("\n-------------------------\n")
