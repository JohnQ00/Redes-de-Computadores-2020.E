import math
import CommandContentAnalysis

LATITUDE = 0
LONGITUDE = 1

pointLocation = []
userLocation = []

def computeDistanceBtwTwoPoints(commandContentFromClient):
    deattachCoordinatesFromCommand(commandContentFromClient)

    R = 6371e+03
    a1 = float(userLocation[LATITUDE]) * 0.01745
    a2 = float(pointLocation[LATITUDE]) * 0.01745
    dt = (float(userLocation[LATITUDE]) - float(pointLocation[LATITUDE])) * 0.01745
    dk = (float(userLocation[LONGITUDE]) - float(pointLocation[LONGITUDE])) * 0.01745

    a_1 = (math.sin(dt / 2) * math.sin(dt / 2))
    a_2 = (math.cos(a1) * math.cos(a2) * math.sin(dk / 2) * math.sin(dk / 2))
    a =  a_1 + a_2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance_untreated = R * c

    outputToClient = []

    if distance_untreated > 1000.0:
        final_distance = distance_untreated / 1000
        final_distance = final_distance.__round__(2)
        outputToClient.append('#165')
        outputToClient.append('The distance between the two points is ' + str(final_distance) + ' km in a straight line')
    else:
        final_distance = final_distance.__round__(0)
        outputToClient.append('#170')
        outputToClient.append('The distance between the two points is ' + str(final_distance) + ' m in a straight line')

    return outputToClient


def deattachCoordinatesFromCommand(commandContentFromClient):
    temporaryList = CommandContentAnalysis.commandContentCheck(commandContentFromClient)
    
    if temporaryList.__len__() == 2:
        temporaryList.insert(0, ' ')
        temporaryList.insert(2, ' ')
        
    userLocation.append(temporaryList[1][0].strip())
    userLocation.append(temporaryList[1][1].strip())

    pointLocation.append(temporaryList[3][0].strip())
    pointLocation.append(temporaryList[3][1].strip())

# print(computeDistanceBtwTwoPoints('a|(-23.533333,-46.616667)|k|(-15.783333,-47.916667)'))
# print(computeDistanceBtwTwoPoints('(-23.533333,-46.616667)|(-15.783333,-47.916667)'))
