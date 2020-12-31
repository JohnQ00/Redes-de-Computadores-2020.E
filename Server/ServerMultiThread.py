import socket
import threading

# Multi thread server using TCP 

print("\nSTARTING MULTITHREAD SERVER\n")
print("Welcome to John's test server, you are in the server side")
print("\n-------------------------\n")

# Setting the socket's address
HOST_AND_PORT = ("localhost", 21000)

# Creating the socket for the server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the socket's address to the socket's instance
serverSocket.bind(HOST_AND_PORT)
serverSocket.listen(6) # Create the number of connections accepted by the server
print("[*] Listen to " + HOST_AND_PORT[0] + ":" + str(HOST_AND_PORT[1]))

def clientHandler(clientSocket):
    dataReceived = clientSocket.recv(1024) # Stabilishes the limit size of the data received from client
    print("[*] Receiving: ", dataReceived.decode())
    print("\n-------------------------\n")
    clientSocket.sendall(dataReceived.upper())
    clientSocket.close()

while True:
    conn, addr = serverSocket.accept() # Store the connection and the address of the client who is connected
    print("[*] Connection accepted by: " + addr[0] + ":" + str(addr[1]))
    threadHandler = threading.Thread(target=clientHandler, args=(conn, ))
    threadHandler.start()
    





