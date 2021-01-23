import csv
import os

storageColumns = ['Username', 'User location', 'Point name', 'Point location']
archiveName = 'Storage.csv'
        
def generateStorage():
    if searchFile(archiveName):
        return
    else:
        try:
            with open(archiveName, 'w', newline='') as csvfile:
                storageWriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                storageWriter.writerow(storageColumns)
        except Exception:
            print(Exception.args)
    
def appendInStorage(dataFromClient):
    try:
        with open(archiveName, 'a', newline='') as csvfile:
            b = csv.writer(csvfile, delimiter=';')
            b.writerow(dataFromClient)
    except PermissionError:
        return '#300'
            
def searchFile(archiveName):
    for file in os.listdir("./"):
        if file.endswith('.csv'):
            return True
    return False

def readStorage():
    markersList = []
    try:
        with open(archiveName, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                markersList.append(row)
    except PermissionError:
        return '#300'
    return markersList
