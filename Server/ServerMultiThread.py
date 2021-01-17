import socket
import threading

# Multi thread server using TCP 

print("\nSTARTING MULTITHREAD SERVER\n")
print("Welcome to John and Hiago's test server, you are in the server side")
print("\n-------------------------\n")

#Creating the command's array and command's content
commands = ['DISCONNECT', 'UPPER']

# Setting the socket's address
HOST_AND_PORT = ("localhost", 22000)

# Creating the socket for the server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the socket's address to the socket's instance
serverSocket.bind(HOST_AND_PORT)
serverSocket.listen(15) # Create the number of connections accepted by the server
print("[*] Listen to " + HOST_AND_PORT[0] + ":" + str(HOST_AND_PORT[1]))  
print("\n-------------------------\n")

def clientHandler(clientSocket):
    while True:
        dataReceived = clientSocket.recv(2048) # Estabilishes the limit size of the data received from client
        print("[*] Receiving: ", dataReceived.decode())
        print("\n-------------------------\n")
        # a(dataReceived, clientSocket)

        if dataReceived.decode() == commands[0]:
            clientSocket.send(str.encode("100 # SHUTTING DOWN THE CONNECTION"))
            clientSocket.close()
            break
        elif dataReceived.decode() == commands[1]:
            clientSocket.send(str.encode("150 # COMMAND ACKNOWLEDGED"))
            dataReceived = clientSocket.recv(1024)
            clientSocket.send(dataReceived.upper())
    return
    
while True:
    conn, addr = serverSocket.accept() # Store the connection and the address of the client who is connected
    print("[*] Connection accepted by: " + addr[0] + ":" + str(addr[1]))
    threadHandler = threading.Thread(target=clientHandler, args=(conn, ))
    threadHandler.start()
