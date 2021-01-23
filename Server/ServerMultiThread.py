import socket
import threading
import CommandContentAnalysis, DistanceCalculus, Storage

# Multi thread server using TCP 
print("\nSTARTING MULTITHREAD SERVER\n")
print("Welcome to localization and distance protocol, you are in the server side")
print("Made by Hiago Lopes and John Dutra")
print("\n-------------------------\n")

#Creating the command's array and command's content
commands = ['DISCONNECT', 'REGISTER', 'READ', 'DISTANCE']
commandDataPartitioned = []
commandAndData = []

# Setting the socket's address
HOST_AND_PORT = ("localhost", 15000)

# Creating the socket for the server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the socket's address to the socket's instance
serverSocket.bind(HOST_AND_PORT)
serverSocket.listen(15) # Create the number of connections accepted by the server

STORAGE_HEADER = "[['Username', 'User location', 'Point name', 'Point location']]"
Storage.generateStorage()

print("[*] Listen to " + HOST_AND_PORT[0] + ":" + str(HOST_AND_PORT[1]))  
print("\n-------------------------\n")

def clientHandler(clientSocket, clientPort):
    while True:
        dataReceived = clientSocket.recv(4096) # :1 Estabilishes the limit size of the data received from client

        if dataReceived == ' ':
            break

        commandAndData = CommandContentAnalysis.commandSplitFromInput(dataReceived.decode())
        
        print("[*] Receiving command " + str(commandAndData[0]) + " from " + str(clientPort[0]) + ":" + str(clientPort[1]))

        if commandAndData[0] == commands[0]:
            clientSocket.send(str.encode(CommandContentAnalysis.commandsCodes[0])) # 2
            clientSocket.close()
            break

        else:
            if commandAndData[0] == commands[1]:
                print("[ Sending:  " + commandAndData[0] + " ]")

                commandDataPartitioned = CommandContentAnalysis.commandContentCheck(commandAndData[1])

                if Storage.appendInStorage(commandDataPartitioned) == CommandContentAnalysis.commandsCodes[2]:
                    clientSocket.send(str.encode('#300'))

                else:
                    if (DistanceCalculus.computeDistanceBtwTwoPoints(commandAndData[1])[0] == CommandContentAnalysis.commandsCodes[5]
                        or DistanceCalculus.computeDistanceBtwTwoPoints(commandAndData[1])[0] == CommandContentAnalysis.commandsCodes[6]):

                        temporaryList = DistanceCalculus.computeDistanceBtwTwoPoints(commandAndData[1])
                        temporaryList.pop(0)

                        clientSocket.send(str.encode('#150 ') + str.encode(temporaryList[0]))

            elif commandAndData[0] == commands[2]:
                dataToSend = str(Storage.readStorage())
                dataToSend = dataToSend.replace(']]', '\n').replace('],', '\n').replace('[', '').replace(']', '').replace('"', '')
                if dataToSend == CommandContentAnalysis.commandsCodes[4]:
                    clientSocket.send(str.encode('#300'))

                elif dataToSend == STORAGE_HEADER and dataToSend != CommandContentAnalysis.commandsCodes[4]:
                    clientSocket.send(str.encode('#310'))

                else:
                    dataToSend = dataToSend.encode()
                    clientSocket.send(str.encode('#155 \n') + dataToSend)
                

            elif commandAndData[0] == commands[3]:
                clientSocket.send(str.encode(DistanceCalculus.computeDistanceBtwTwoPoints(commandAndData[1])[0] + ' ')  +
                str.encode(DistanceCalculus.computeDistanceBtwTwoPoints(commandAndData[1])[1]))
                
    return

while True:
    conn, addr = serverSocket.accept() # Store the connection and the address of the client who is connected
    print("[*] Connection accepted by: " + addr[0] + ":" + str(addr[1]))
    threadHandler = threading.Thread(target=clientHandler, args=(conn, addr))
    threadHandler.start()
