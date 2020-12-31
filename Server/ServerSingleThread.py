import socket

# Single thread server using TCP 

print("\nSTARTING SINGLE THREAD SERVER\n")
print("Welcome to John's test server, you are in the server side")
print("\n-------------------------\n")

# Setting the socket's address
HOST_AND_PORT = ('localhost', 20000)

# Creating the socket for the server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the socket's address to the socket's instance
serverSocket.bind(HOST_AND_PORT)
serverSocket.listen() # Create the number of connections accepted by the server
print("[*] Listen to " + HOST_AND_PORT[0] + ":" + str(HOST_AND_PORT[1]))
conn, addr = serverSocket.accept() # Store the connection and the address of the client who is connected
print("[*] Connected to: ", addr)

while True:
    dataReceived = conn.recv(1024) # Stabilishes the limit size of the data received from client
    if not dataReceived:
        print("Closing the connection")
        conn.close() # Close the connection
        break
    conn.sendall(dataReceived.upper()) # Send all the data received from client back to it
