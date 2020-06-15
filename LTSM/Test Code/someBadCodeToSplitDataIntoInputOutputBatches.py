import numpy as np
from itertools import chain
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from matplotlib import pyplot as plt
import math  

#array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
#array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21],[22, 23, 24], [25, 26, 27]]])
array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]], [[25, 26, 27, 28],[29, 30, 31, 32], [33, 34, 35, 36]]])
#array = np.zeros((140, 64, 56))

xSize= 2
ySize = 1

def minVal(n):
  return (n // 2) * 2

X, Y, Z = array.shape
print(array.shape)

#Set new array shape
#X, Y, Z = minVal(X), Y, 2

print("\nZ: " , len(array[0][0]), Z)
print("\nY: " , len(array[0]), Y)
print("\nX: " , len(array), X)


val = list()

for x in range(X):
  for z in range(Z):
    for y in range(Y):
      val.append(array[x][y][z])

print(array)
print(val)


xInputs = list()
xOutputs = list()
chunkLength = Y*xSize
maxX = Y*Z
iterations = Z-(xSize+ySize) + 1 #calculates possible batch iterations

print(Y*xSize)
print(maxX)

print(iterations)
for k in range(iterations):
  pos = (k*Y) #where to begin from
  

  xInSeq = list()
  xOutSeq = list()
  while(pos < (len(val))):
    xInSeq.append(val[pos:pos + chunkLength])
    print(pos , val[pos:pos + chunkLength], chunkLength)

    xOutSeq.append(val[pos + chunkLength:pos + chunkLength+(ySize*Y)])
    pos = pos + maxX 

  
  newXInSeq = list(chain.from_iterable(xInSeq)) 
  newXOutSeq = list(chain.from_iterable(xOutSeq)) 

    

  xInputs.append(newXInSeq)
  xOutputs.append(newXOutSeq)

xI = np.array(xInputs)
xO = np.array(xOutputs)


#print(xInSeq)
#print(xOutSeq)
print(xInputs)
print(xOutputs)

n_features = 1
xI = xI.reshape((xI.shape[0], xI.shape[1], n_features))
# define model
model = Sequential()
model.add(LSTM(100, activation='relu', return_sequences=True, input_shape=(int(chunkLength*X) , n_features)))
model.add(LSTM(100, activation='relu'))
model.add(Dense(Y*ySize*X))
model.compile(optimizer='adam', loss='mse')

# fit model
model.fit(xI, xO, epochs=200, verbose=1)
# demonstrate prediction

x_input = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
x_input2 = x_input.reshape((1, int(chunkLength*X) , n_features))
y_output = model.predict(x_input2, verbose=0)

print(y_output)






