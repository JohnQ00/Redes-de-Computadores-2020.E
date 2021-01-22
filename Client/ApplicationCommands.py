import re
commandsDictionary = ['DISCONNECT', 'REGISTER', 'READ', 'DISTANCE']
commandsCodes = ['#100', '#150', '#300', '#155', '#310', '#165', '#170', '#320']
# disconnect, register successful, read successful and distance successful
commandFromClient = []

def checkCommand(inputFromClient):
    commandFromClient = inputFromClient.split('#')

    if commandFromClient[0] == commandsDictionary[0] or commandFromClient[0] == commandsDictionary[2]:
        return True
    elif commandFromClient[0].strip() == commandsDictionary[1] or commandFromClient[0].strip() == commandsDictionary[3]:
        if inputFromClient.find('#') != -1:
            if commandFromClient.__len__() > 1:
                if commandFromClient[1] != '':
                    if commandFromClient[0].strip() == commandsDictionary[1]:
                        if commandFromClient[1].count('|') == 3:
                            return checkIfThereIsACoordinate(commandFromClient[1])
                        else:
                            return False
                    elif commandFromClient[0].strip() == commandsDictionary[3]:
                        if commandFromClient[1].count('|') == 1:
                            return checkIfThereIsACoordinate(commandFromClient[1])
                        else:
                            return False
                else:
                    return False
            elif commandFromClient.__len__() <= 1:
                return False
        else:
            return False
    else:
        return False
    
def CommandContentHelper(commandFromClient):
    commandHelpers = {
        commandsDictionary[1]: 
        "Follow this model: REGISTER#'Name'|'(Your latitude, Your longitude)'|'Marking point name'|'(Point latitude, Point longitude)'",
        commandsDictionary[3]:
        "Follow this model: DISTANCE#'(Your latitude, Your longitude)'|'(Point latitude, Point longitude)'",
        ' ':
        'You typed a blank space'
    }

    print("\n" + commandHelpers.get(commandFromClient.split('#')[0].strip(), "This command does not need a model"))

def checkIfThereIsACoordinate(commandFromClient):
    temporaryList = commandFromClient.split('|')
    
    if temporaryList[0] == '' or temporaryList[1] == '':
        return False

    elif temporaryList.__len__() == 2:
        temporaryList.insert(0, ' ')
        temporaryList.insert(2, ' ')

    return regexChecker(temporaryList)

def regexChecker(temporaryList):
    if re.search("[a-zA-Z]", temporaryList[1]) == None and re.search("[a-zA-Z]", temporaryList[3]) == None:
        return True
    elif re.search("[0-9]", temporaryList[1]) != None and re.search("[0-9]", temporaryList[3]) != None:
        return False



# elif commandFromClient[0].strip() != command:
#     return False



# if inputFromClient.find('#') != -1:
#                 print("aiaiaa")
#                 if commandFromClient.__len__() != 1:
#                     print("pinto")
#                     return False
#                 elif commandFromClient.__len__() == 1:
#                     print("prexeca")
#                     return False
#             else:
#                 return False