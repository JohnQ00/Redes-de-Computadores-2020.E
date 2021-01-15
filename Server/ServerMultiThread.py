import socket
import threading

# Multi thread server using TCP 

print("\nSTARTING MULTITHREAD SERVER\n")
print("Welcome to John's test server, you are in the server side")
print("\n-------------------------\n")

#Creating the command's array and command's content
commands = ['DISCONNECT', 'UPPER']
commandContent = ['UPPER#']
# Setting the socket's address
HOST_AND_PORT = ("localhost", 21000)

# Creating the socket for the server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the socket's address to the socket's instance
serverSocket.bind(HOST_AND_PORT)
serverSocket.listen(15) # Create the number of connections accepted by the server
print("[*] Listen to " + HOST_AND_PORT[0] + ":" + str(HOST_AND_PORT[1]))  
print("\n-------------------------\n")

def clientHandler(clientSocket):
    dataReceived = clientSocket.recv(1024) # Stabilishes the limit size of the data received from client
    print("[*] Receiving: ", dataReceived.decode())
    print("\n-------------------------\n")
    if dataReceived.decode() == commands[0]:
        clientSocket.sendall(str.encode("100 # SHUTTING DOWN THE CONNECTION"))
        clientSocket.close()
        return
    elif dataReceived.decode() == commands[1]:
        clientSocket.sendall(str.encode("200 # CONNECTION STABILISHED"))
        c = clientSocket.recv(1024)
        clientSocket.sendall(c.upper())
    
while True:
    conn, addr = serverSocket.accept() # Store the connection and the address of the client who is connected
    print("[*] Connection accepted by: " + addr[0] + ":" + str(addr[1]))
    threadHandler = threading.Thread(target=clientHandler, args=(conn, ))
    threadHandler.start()
