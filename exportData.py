import csv

#append new data to data file
def _writeData(newData,filename):
    with open(filename, 'w',newline="") as csvfile:
        #create writer
        csvwriter = csv.writer(csvfile)
        #append new rows
        csvwriter.writerow(newData)

def _writeDataA(newData,filename):
    with open(filename, 'a',newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(newData)

def printThing(string):
        print(string)