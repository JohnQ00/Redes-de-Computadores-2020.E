commands = ['DISCONNECT', 'REGISTER', 'READ', 'DISTANCE']
commandsCodes = ['#100', '#150', '#300', '#155', '#310', '#165', '#170', '#320']
temporaryCommandSplit = []

def commandContentCheck(commandContentFromClient):
    dataWrittenByClient = []
    informationFromClient = []
    contentCounter = 0

    commandDataFromClient = str(commandContentFromClient).replace(" ", "").split('|')
    while contentCounter != str(commandContentFromClient).split('|').__len__():
        if commandDataFromClient[contentCounter][0] == '(' and commandDataFromClient[contentCounter][-1] == ')':
            #aqui precisa de uma verificação
            dataWrittenByClient.append(
                commandDataFromClient[contentCounter].
                strip('(').
                strip(')').
                split(',')
            )
        else:
            dataWrittenByClient.append(commandDataFromClient[contentCounter])
        contentCounter = contentCounter + 1
    return dataWrittenByClient

def commandSplitFromInput(inputFromClient):
    commandFromClient = []
    temporaryCommandSplit = inputFromClient.split('#')
    if temporaryCommandSplit[0] == commands[1] or temporaryCommandSplit[0] == commands[3]:
        commandFromClient.append(temporaryCommandSplit[0].strip())
        commandFromClient.append(temporaryCommandSplit[1].strip())
    else:
        commandFromClient.append(temporaryCommandSplit[0].strip())
    return commandFromClient

# print(commandContentCheck('John|Ponto|(1.5555, 1.6665)|(1.552255, 1.6688865)'))
# print(commandSplitFromInput('REGISTER # John|Ponto|(1.5555, 1.6665)|(1.552255, 1.6688865)'))
