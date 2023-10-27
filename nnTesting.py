import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model

import cv2
import os
import random
import exportData
import time

DATADIR = "neuralNetwork/testingData/Busy/"
CATEGORIES = ["Bells","Knock","Instrument","Talk"]

# 0 = bell, 1 = knock, 2 = inst, 3 = talk

training_data = []

def createTrainingData(type):
    for category in CATEGORIES:
      path = os.path.join(DATADIR,category)
      class_num = CATEGORIES.index(category)
      for img in os.listdir(path):
        img2 = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        img2 = cv2.resize(img2,(38,28))
        img2 = img2.astype('float32')
        if(type == 'f'):
          img2 = img2.reshape(-1,38*28)
        else:
          img2 = img2.reshape(-1,38,28,1)
        img2 /=255
        training_data.append([img2, class_num])

def testNN(type):
  random.shuffle(training_data)

  X = []
  y = []

  imX = 38
  imY = 28

  for features, label in training_data:
      X.append(features)
      y.append(label)

  nnAnswer = []
  nnChoice = []
  nnTime = []
  model = load_model('models/' + type + '.h5')
  i = 0
  for i in range(100):
      rand = random.randint(0, len(y)-1)

      initialTime = time.time()
      prediction = model.predict(X[rand])
      finalTime = time.time()
      deltaT = finalTime - initialTime
      print(deltaT)
      pred = str(np.argmax(prediction,axis=1))

        #remove brackets
      pred = pred.replace('[','')
      pred = pred.replace(']','')

      actualPrediction = CATEGORIES[int(pred)]
      print(actualPrediction)
      print(CATEGORIES[y[rand]])
      answer = CATEGORIES[y[rand]]

      nnChoice.append(actualPrediction)
      nnAnswer.append(answer)
      nnTime.append(deltaT)

  exportData._writeDataA(nnAnswer, "data/nn/" + type + "Answer.csv")
  exportData._writeDataA(nnChoice, "data/nn/" + type + "Choice.csv")
  exportData._writeDataA(nnTime,"data/nn/" +  type + "Time.csv")

createTrainingData('f')


for num in range(1,21):
  num *= 5
  print(num)
  testNN('ffnnd.01' + str(num))
  