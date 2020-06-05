from nbtschematic import SchematicFile
import numpy as np


sf = SchematicFile.load('chunk1.schematic')

print(sf.blocks[255, -15, 15])
breakpoint
blocks = np.arange(128*16*16).reshape(128,16,16)

for x in range(128):
    for z in range(16):
        for y in range(16):
            blocks[x][z][y] = sf.blocks[x,z,y]

print(blocks)

import numpy as np
from itertools import chain
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from matplotlib import pyplot as plt
import math  

#array = np.array([[[1, 2, 3]], [[4,5,6]]])
#array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
#array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21],[22, 23, 24], [25, 26, 27]]])
array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]], [[25, 26, 27, 28],[29, 30, 31, 32], [33, 34, 35, 36]]])
array = np.zeros((140, 64, 56))

global xSize
xSize= 2
ySize = 2

def flatten(array, Z, Y, X ):

	val = list()
	for z in range(Z):
		for x in range(X):
			for y in range(Y):
				val.append(array[z][y][x])
	return val

def minVal(n):
  return (n // xSize) * xSize

def plump(Z, Y, X, val):

	array = np.zeros((Z, Y, X))
	for z in range(Z):
		for x in range(X):
			for y in range(Y):
				array[z, y, x]=int(val[y+(x*Y)+(z*Y*X)])
	return array

Z, Y, X = array.shape
print(array.shape)

#Set new array shape
Z, Y, X = xSize, Y, minVal(X)

print("\nZ: " , len(array[0][0]), Z)
print("\nY: " , len(array[0]), Y)
print("\nX: " , len(array), X)



val = flatten(array, Z,Y,X)

xInputs, xOutputs = list(),list()

#print(array)
#print(val)

new=plump(Z,Y,X, val)


#determine info from data
chunkLength = Y*xSize
maxX = Y*X
iterations = X-(xSize+ySize) + 1 #calculates possible batch iterations

#
print(Y*xSize)
print(maxX)

print(iterations)

for k in range(iterations):
  pos = (k*Y) #where to begin from
  
  xInSeq = list()
  xOutSeq = list()
  while(pos < (len(val))):
    xInSeq.append(val[pos:pos + chunkLength])
    #print(pos , val[pos:pos + chunkLength], chunkLength)

    xOutSeq.append(val[pos + chunkLength:pos + chunkLength+(ySize*Y)])
    pos = pos + maxX 

  
  newXInSeq = list(chain.from_iterable(xInSeq)) 
  newXOutSeq = list(chain.from_iterable(xOutSeq)) 

    

  xInputs.append(newXInSeq)
  xOutputs.append(newXOutSeq)

xInputs = np.array(xInputs)
xOutputs = np.array(xOutputs)


#print(xInSeq)
#print(xOutSeq)
print(xInputs)
print(xOutputs)


flag1=1
while flag1==1:
	n_features = 1
	xInputs = xInputs.reshape((xInputs.shape[0], xInputs.shape[1], n_features))
	# define model
	model = Sequential()
	model.add(LSTM(100, activation='relu', return_sequences=True, input_shape=(int(chunkLength*Z) , n_features)))
	model.add(LSTM(100, activation='relu'))
	model.add(Dense(Y*ySize*Z))
	model.compile(optimizer='adam', loss='mse')

	# fit model
	model.fit(xInputs, xOutputs, epochs=200, verbose=2)
	# demonstrate prediction

	x_input = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
	x_input2 = x_input.reshape((1, int(chunkLength*Z) , n_features))
	y_output = model.predict(x_input2, verbose=0)

	print(y_output)
 
	print(plump())
	flag1=2 






