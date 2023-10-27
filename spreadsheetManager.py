import csv
import exportData as e
#-----------participant section----------------


def partTime():
    participantTime = []
    avgReactTime = []
    #get each participants' average reaction time

    with open('data/human/reactionTimeData.csv',newline='') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        lineCount = 0
        for row in csv_reader:
            participantTime.append(row)


    for row in participantTime:
        sum = 0
        for col in row:
            sum += float(col)
        avgReactTime.append(float(sum/5))


    decisionTimes = []
    adjDecisionTimes = []
    with open('data/human/trialTimeData.csv',newline='') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        lineCount = 0
        for row in csv_reader:
            decisionTimes.append(row)

    rowNum = 0
    for row in decisionTimes:
        
        tempList = []
        for col in row:
            tempList.append(float(col)-avgReactTime[rowNum])
        rowNum += 1
        adjDecisionTimes.append(tempList)


    overallAvgTime = []
    noneAvgTime = []
    wnAvgTime =[]
    envrnAvgTime =[] 
    bsyAvgTime =[]

    rowNum = 0
    for row in adjDecisionTimes:
        colNum = 0
        for col in row:
            
            overallAvgTime.append(float(col))
            if(colNum > 14):
                bsyAvgTime.append(float(col))
            elif(colNum > 9):
                envrnAvgTime.append(float(col))
            elif(colNum > 4):
                wnAvgTime.append(float(col))
            else:
                noneAvgTime.append(float(col))
            colNum += 1
        rowNum +=1

    times = []

    sum = 0
    for num in overallAvgTime:
        sum += num / len(overallAvgTime)

    times.append(sum)

    sum = 0
    for num in noneAvgTime:
        sum += num / len(noneAvgTime)

    times.append(sum)

    sum = 0
    for num in wnAvgTime:
        sum += num / len(wnAvgTime)

    times.append(sum)

    sum = 0
    for num in envrnAvgTime:
        sum += num / len(envrnAvgTime)

    times.append(sum)

    sum = 0
    for num in bsyAvgTime:
        sum += num / len(bsyAvgTime)

    times.append(sum)

    e._writeData(times, 'data/human/partTimes.csv')


def partAcc():
    choiceData = []
    correctData = []
    with open('data/human/trialChoiceData.csv',newline='') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        lineCount = 0
        for row in csv_reader:
            choiceData.append(row)

    with open('data/human/trialCorrectData.csv',newline='') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        lineCount = 0
        for row in csv_reader:
            correctData.append(row)

    temAns = []

    #amount of articiants 
    amount = len(choiceData)
    #amount of data from each articiant
    dataNum = 20

    i = 0
    j = 0

    for i in range(amount):
        currentChoice = choiceData[i]
        currentCorrect = correctData[i]
        temAccurate = []
        for j in range(dataNum):
            if(currentChoice[j].lower() == currentCorrect[j].lower()):
                temAccurate.append(1)
            else:
                temAccurate.append(0)
            j+=1
        temAns.append(temAccurate)
        i+=1



    overallAvgAcc = []
    noneAvgAcc = []
    wnAvgAcc =[]
    envrnAvgAcc =[] 
    bsyAvgAcc =[]

    rowNum = 0
    for row in temAns:
        colNum = 0
        for col in row:
            
            overallAvgAcc.append(float(col))
            if(colNum > 14):
                bsyAvgAcc.append(float(col))
            elif(colNum > 9):
                envrnAvgAcc.append(float(col))
            elif(colNum > 4):
                wnAvgAcc.append(float(col))
            else:
                noneAvgAcc.append(float(col))
            colNum += 1
        rowNum +=1

    acc = []

    sum = 0
    for num in overallAvgAcc:
        sum += num / len(overallAvgAcc)

    acc.append(sum)

    sum = 0
    for num in noneAvgAcc:
        sum += num / len(noneAvgAcc)

    acc.append(sum)

    sum = 0
    for num in wnAvgAcc:
        sum += num / len(wnAvgAcc)

    acc.append(sum)

    sum = 0
    for num in envrnAvgAcc:
        sum += num / len(envrnAvgAcc)

    acc.append(sum)

    sum = 0
    for num in bsyAvgAcc:
        sum += num / len(bsyAvgAcc)

    acc.append(sum)


    e._writeData(acc, 'data/human/partAcc.csv')

############## NEURAL NETWORKS ##############



def manageNNTime(type):
    nnTime = []
    with open('data/nn/' + type + 'Time.csv', newline='') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        lineCount = 0
        for row in csv_reader:
            nnTime.append(row)

    overallBG = 0
    noBG = 0
    wnBG = 0
    enBG = 0
    bsBG = 0



    amount = 100
    
    i = 0
    for row in nnTime:
        
        for col in row:
            overallBG += float(col) / (amount * 4)
            if(i == 0):
                noBG += float(col) / amount
            elif(i == 1):
                wnBG += float(col) / amount
            elif(i == 2):
                enBG += float(col) / amount
            elif(i == 3):
                bsBG += (float(col) / amount)
        i += 1  
    
    times = [overallBG,noBG,wnBG,enBG,bsBG]
    e._writeData(times, 'results/nn/' + type + '_times.csv')
    

def manageNNAcc(type):
    correct = []
    choice = []

    with open('data/nn/' + type + 'Answer.csv',newline='') as csv_file:
        csv_reader=csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            correct.append(row)
    with open('data/nn/' + type + 'Choice.csv',newline='') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            choice.append(row)
    
    amount = 100
    bgAmnt = 4

    overallBG = 0
    noBG = 0
    wnBG = 0
    enBG = 0
    bsBG = 0

    i = 0
    j = 0
    for i in range(len(correct)):
        tmpArrCor = correct[i]
        tmpArrChc = choice[i]
        for j in range(amount):
            if(tmpArrChc[j] == tmpArrCor[j]):
                if(i == 0):
                    noBG += (1 / amount)
                elif(i == 1):
                    wnBG += (1 / amount)
                elif(i == 2):
                    enBG += (1 /amount)
                else:
                    bsBG += (1 /amount)
            j += 1
        i += 1
    
    overallBG = (noBG + wnBG + enBG + bsBG) / 4

    acc = [overallBG,noBG,wnBG,enBG,bsBG]
    e._writeData(acc, 'results/nn/' + type + '_acc.csv')
    

def combineData(type,t):
    data = []
    with open('results/nn/' + type + '_acc.csv',newline='') as csv_file:
        csv_reader=csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(row)
    
    adjData = []

    for da in data:
        for d in da:
            d = d.replace('[','')
            d = d.replace(']','')
            adjData.append(d)

    e._writeDataA(adjData, t)

for i in range(1,21):
    i*=5
    combineData('ffnnd.01' + str(i), 'ffnnd01')