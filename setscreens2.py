import tkinter as tk
from playsound import playsound
import exportData
import time
import random
from threading import Thread
import psutil
from multiprocessing import Process
import os

root = tk.Tk()
root.attributes('-fullscreen', True)

#sets column and row sizes for grid layout
root.columnconfigure(0,weight =1)
root.columnconfigure(1,weight= 1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.columnconfigure(4,weight=1)
root.rowconfigure(0,weight =1)
root.rowconfigure(1,weight = 1)
root.rowconfigure(2,weight =1)

#putting all the label strings as variables here so they dont look messy"Information about the trial"
beforeTest = "Next you can listen to the test sounds before you have to categorize them. Press continue when you are ready."
soundDemo = "Click the buttons to hear what audio in that category sounds like"

global buttonClicked
buttonClicked = False

#main screen
def setScreenHome():
    clearScreen(root)
    makeHeader("Categoriazation Test")

    #global variable for entered user number
    global userNum 
    userNum = tk.StringVar()
    #entry box for user number
    userNumber = tk.Entry(root,textvariable=userNum)
    userNumber.grid(column = 2, row =1)
    userNumber.focus()

    enterUserNum = tk.Button(root,text = "ENTER", command=setScreenMenu)
    enterUserNum.grid(column=2,row=2)

    addExitButton()
    root.mainloop()

#menu to navigate to test and see data
def setScreenMenu():
    uNum = userNum.get()
    clearScreen(root)
    makeHeader("Categorization Test")
    doTrialButton = tk.Button(root,text = "Do Trial",command=setScreenTrialInfo)
    doTrialButton.grid(column=2,row=1)

    userNumLabel = tk.Label(root,text = uNum)
    userNumLabel.grid(column=2,row=2)

    addExitButton()

#screen that has information about the test, lets you hear the sound
#and takes you to the start test screen


#information before starting the test and listening
def setScreenTrialInfo():
    clearScreen(root)

    makeHeader("")

    #info
    someMoreInfo = tk.Label(root, text=beforeTest)
    someMoreInfo.grid(column=2,row=1)

    #cont button
    continueButton = tk.Button(root,text="Continue", command=setScreenListen)
    continueButton.grid(column=4,row=2)

#screen for listening to training data
def setScreenListen():
    clearScreen(root)
    makeHeader(soundDemo)

    bellButton = tk.Button(root,text="bell",command=testBell)
    bellButton.grid(column=0,row=1)

    knockButton = tk.Button(root,text="knock",command=testKnock)
    knockButton.grid(column = 1, row =1)

    instButton = tk.Button(root,text = "instrument", command=testInst)
    instButton.grid(column=2,row=1)

    talkButton = tk.Button(root,text="talking",command=testTalk)
    talkButton.grid(column=3,row =1)

    continueButton = tk.Button(root,text="Continue to test",command=setScreenTrial)
    continueButton.grid(column=4,row=2)

#screen for the actual test
def setScreenTrial():
    clearScreen(root)

    makeHeader("Click the button when you think you hear the sound")

    startButton = tk.Button(root,text="START",command = startThreadTest)
    startButton.grid(column =2,row=0)

    bellButton = tk.Button(root,text="bell",command = heardBell)
    bellButton.grid(column=0,row=1)

    knockButton = tk.Button(root,text="knock",command = heardKnock)
    knockButton.grid(column = 1,row=1)

    instButton = tk.Button(root,text="instrument",command=heardInst)
    instButton.grid(column=2,row=1)

    talkButton = tk.Button(root,text ="talking",command=heardTalk)
    talkButton.grid(column=3,row=1)

    #get rid of later
    addExitButton()

def setScreenDone():
    clearScreen(root)
    
    done = tk.Label(root,text="You have completed the test")
    done.grid(column=2,row=1)

    addExitButton()

#playing the demo sounds

#random pick sound from training bells, but need audio so only bell1
def testBell():
    audioFile = random.choice(os.listdir("audio/testing/bell"))
    playsound("audio/testing/bell/" + audioFile)

def testKnock():
    audioFile = random.choice(os.listdir("audio/testing/knock"))
    playsound("audio/testing/knock/" + audioFile)

def testInst():
    audioFile = random.choice(os.listdir("audio/testing/inst"))
    playsound("audio/testing/inst/" + audioFile)

def testTalk():
    audioFile = random.choice(os.listdir("audio/testing/talk"))
    playsound("audio/testing/talk/" + audioFile)

#buttons for hearing the test sounds
def heardBell():
    setBellHeard(True)
    setButtonClick(True)
    setChosen("Bell")

def setBellHeard(bool):
    global bellHeard
    bellHeard = bool

def getBellHeard():
    return bellHeard

def heardKnock():
    setKnockHeard(True)
    setButtonClick(True)
    setChosen("Knock")

def setKnockHeard(bool):
    global knockHeardbool
    knockHeard = bool
   

def getKnockHeard():
    return knockHeard

def heardInst():
    setInstHeard(True)
    setButtonClick(True)
    setChosen("Inst")

def setInstHeard(bool):
    global instHeard
    instHeard = bool

def getInstHeard():
    return instHeard

def heardTalk():
    setTalkHeard(True)
    setButtonClick(True)
    setChosen("Talk")

def setTalkHeard(bool):
    global talkHeard
    talkHeard = bool

def getTalkHeard():
    return talkHeard

#exit button 
def addExitButton():
    exitButton = tk.Button(root, text = "EXIT", command = root.destroy)
    exitButton.grid(column=4,row = 2)

#clears all widgets from the screen
def clearScreen(window):
    list = window.winfo_children()

    for item in list:
        item.destroy()

#makes the header with parameter of the text
def makeHeader(titleText):
    headerMain = tk.Label(root, text = titleText)
    headerMain.grid(column = 0, row=0)

#plays the bell sound for reaction time test
def playDemoSound():
    playsound('audio/bell1.wav')

#test for reaction time
def reactTest():
    #boolean for whether the sound has already been played for no button spam
    setPlayedSound(False)
    #time data
    data = []
    data.append(userNum.get())
    #low time for test (seconds)
    low = 3
    #high time for test (sec)
    high = 7

    i = 0
    
    for i in range(5):
        time.sleep(getRandTime(low,high))
        setPlayedSound(True)
        initTime = time.time()
        #print(initTime)

        playsound('audio/bell1.wav',False)
        while(getPlayedSound() == True):
            if(getButtonClick() == True):
                finalTime = time.time()
                #print(finalTime)
                setButtonClick(False)
                setPlayedSound(False)

        deltaTime = finalTime - initTime
        data.append(deltaTime)
        i = i + 1
    exportData._writeData(data,'reactionTimeData.csv')
    setTesting(False)
    time.sleep(3)
    print("done")
    


#used to gen rand time in range low - high for react test
def getRandTime(low,high):
    return random.randrange(low,high)


#set whether a button was clicked
def setButtonClick(bool):
    global buttonClicked
    buttonClicked = bool

#was a button  clicked
def getButtonClick():
    return buttonClicked

#set whether a sound was played 
def setPlayedSound(bool):
    global soundPlayed
    soundPlayed = bool

#what does it look like the function does?
def getPlayedSound():
    return soundPlayed

#another thread for while loops in trial
def startThreadTest():
    t2 = Thread(target=trial)
    t2.start()

def setChosen(name):
    global chosen
    chosen = name

def getChosen():
    return chosen

#the trial, basically same as reaction time test
def trial():
    global buttonClicked
    setButtonClick(False)
    #boolean for whether a sound has already been played for no button spam
    setPlayedSound(False)

    #time data
    dataTime = []
    dataTime.append(userNum.get())

    #user choice data
    dataChosen = []
    dataChosen.append(userNum.get())

    #correct answer data
    dataCorrect = []
    dataCorrect.append(userNum.get())

    #low time for test (seconds)
    low = 3
    #high time for test (sec)
    high = 7

    i = 0
    j = 0
    #for the 4  types of noise backgroudn
    for i in range(4):
        #for the 5 different sounds played per background
        #change this based on background
        
        bg=""

        if(i==0):
            bg = "audio/backgrounds/nothing.wav"
        elif(i == 1): #fix file extensions its fine now 
            bg = "audio/backgrounds/whitenoise.mp3"
        elif(i == 2):
            bg = "audio/backgrounds/environment.mp3"
        elif(i==3):
            bg = "audio/backgrounds/busy.mp3"
        #playingBackgrounds(bg)
        #playsound(bg,False)
        #process for playing the background sound
        print(bg)
        p = Process(target=playingBackgrounds,args=(bg,))
        p.start()
        for j in range(5):

            type = random.randint(0,3)
            
            if (type == 0):
                category = "bell"
            elif (type == 1):
                category = "inst"
            elif (type == 2):
                category = "knock"
            else:
                category = "talk"

            dataCorrect.append(category)
            
            audioFile = random.choice(os.listdir("audio/testing/" + category))
            time.sleep(getRandTime(low,high))
            
            initTime = time.time()
            #print(initTime)

            #instead play random test data
            #append sound category into dataCorrect
            setButtonClick(False)
            setPlayedSound(True)
            audioFile2 = "audio/testing/" + category + "/" + audioFile + "/"
            p2 = Process(target=playingBackgrounds2,args=(audioFile2,))
            p2.start()
            #playsound(audioFile2)
            print("played")
            while(getPlayedSound() == True):
                #when a button is clicked, not specific one now
                testTime = time.time()
                if(getButtonClick() == True or testTime - initTime > 10):
                    p2.terminate()
                    print("clicked")
                    if(getButtonClick() == True):
                        dataChosen.append(getChosen())
                        finalTime = time.time()
                    else:
                        dataChosen.append(" ")
                        finalTime = time.time()
                    #print(finalTime)
                    #append chosen
                    setButtonClick(False)
                    setPlayedSound(False)

            deltaTime = finalTime - initTime
            dataTime.append(deltaTime)
            j= j+1
        i = i + 1
        #stop process when background is done
        time.sleep(1)
        p.terminate()
    #write all of the trial data
    exportData._writeData(dataTime,'trialTimeData.csv')
    exportData._writeData(dataChosen, 'trialChoiceData.csv')
    exportData._writeData(dataCorrect, 'trialCorrectData.csv')
    setScreenDone()

#func for thread to play background audio and the sounds because im lazy and it broke when i made a new one
def playingBackgrounds(file):
    playsound(file)

def playingBackgrounds2(file):
    playsound(file)
