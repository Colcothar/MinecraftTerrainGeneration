from nbtschematic import SchematicFile
import numpy as np

from itertools import chain
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from matplotlib import pyplot as plt
import math

def makeArray(location):
    sf = SchematicFile.load(location)

    Y = len(sf.blocks)
    Y = 32
    Z = len(sf.blocks[0])
    X = len(sf.blocks[0][0])

    breakpoint
    array = np.zeros(Z*Y*X).reshape(Z, Y, X)

    for y in range(Y):
        for z in range(Z):
            for x in range(X):
                array[z,y,x] = sf.blocks[y,z,x]
    return array



# array = np.array([[[1, 2, 3]], [[4,5,6]]])
# array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
# array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21],[22, 23, 24], [25, 26, 27]]])
# array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]], [[25, 26, 27, 28],[29, 30, 31, 32], [33, 34, 35, 36]]])
# array = np.zeros((140, 64, 56))


#print(array)

array = makeArray('/home/ist/Desktop/AI/Minecraft/2048.schematic')

global xSize
xSize = 2
ySize = 2


def flatten(array, Z, Y, X):

	val = list()
	for z in range(Z):
		for x in range(X):
			for y in range(Y):
				val.append(array[z][y][x])
	return val


def minVal(n):
  return (n // xSize) * xSize


def plump(Z, Y, X, val, format):

    array = np.zeros((Z, Y, X))
    for z in range(Z):
        for x in range(X):
            for y in range(Y):
                if format == False:
                    array[z, y, x] = val[y+(x*Y)+(z*Y*X)]
                elif format == True:
                    temp = int(val[y+(x*Y)+(z*Y*X)])
                    if temp < 0:
                        temp = 0
                    elif temp > 255:
                        temp = 255
                    array[z, y, x] = temp

    return array

Z, Y, X=array.shape

#print("\nZ: ",  Z)
#print("\nY: ",  Y)
#print("\nX: ",  X)

# Set new array shape
Z, Y, X=16, Y, minVal(X)

print("\nZ: ",  Z)
print("\nY: ",  Y)
print("\nX: ",  X)



val=flatten(array, Z, Y, X)

xInputs, xOutputs=list(), list()

# print(array)
# print(val)

new=plump(Z, Y, X, val, False)


# determine info from data
chunkLength=Y*xSize
maxX=Y*X
iterations=X-(xSize+ySize) + 1  # calculates possible batch iterations

#
print(Y*xSize)
print(maxX)

print(iterations)

for k in range(iterations):
  pos=(k*Y)  # where to begin from

  xInSeq=list()
  xOutSeq=list()
  while(pos < (len(val))):
    xInSeq.append(val[pos:pos + chunkLength])
    # print(pos , val[pos:pos + chunkLength], chunkLength)

    xOutSeq.append(val[pos + chunkLength:pos + chunkLength+(ySize*Y)])
    pos=pos + maxX


  newXInSeq=list(chain.from_iterable(xInSeq))
  newXOutSeq=list(chain.from_iterable(xOutSeq))



  xInputs.append(newXInSeq)
  xOutputs.append(newXOutSeq)

xInputs=np.array(xInputs)
xOutputs=np.array(xOutputs)


# print(xInSeq)
# print(xOutSeq)
print(xInputs)
print(xOutputs)


flag1=1
while flag1 == 1:

    n_features=1
    xInputs=xInputs.reshape((xInputs.shape[0], xInputs.shape[1], n_features))
	# define model
    model=Sequential()
    model.add(LSTM(10, activation='relu', return_sequences=True,
              input_shape=(int(chunkLength*Z), n_features)))
    model.add(LSTM(10, activation='relu'))
    model.add(Dense(Y*ySize*Z))
    model.compile(optimizer = 'adam', loss = 'mse')
    model.save('model')

    filepath = "checkpoint.h5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]

	# fit model
    model.fit(xInputs, xOutputs, epochs = 200, verbose = 2, callbacks=callbacks_list)
	# demonstrate prediction
    model = keras.models.load_model('model')

       
    x_input=np.array(flatten(makeArray('/home/ist/Desktop/AI/Minecraft/32.schematic'), Z,Y,xSize))          
    x_input2=x_input.reshape((1, int(chunkLength*Z), 1))
    y_output=model.predict(x_input2, verbose = 0)


    y_output3d = plump(Z, Y, ySize, y_output[0], True)

    print(plump(Z, Y, ySize, y_output[0], False))
    print(y_output3d)

    sf = SchematicFile(shape=(Z, Y, ySize))
    assert sf.blocks.shape == (Z,Y, ySize)


    sf.blocks= y_output3d
    sf.save('example.schematic')


    flag1=2
