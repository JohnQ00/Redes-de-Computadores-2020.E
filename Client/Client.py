import socket

print("\nSTARTING CLIENT\n")
print("Welcome to John's test server, you are in the client side\n")

HOST_AND_PORT = ('localhost', 20000)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(HOST_AND_PORT)
textToSend = input("Type the message you want to send: ")
clientSocket.sendall(str.encode(textToSend))
data = clientSocket.recv(1024)

print("\nMessage succesfully echoed: \n", data.decode())

