from nbtschematic import SchematicFile
import numpy as np

def makeArray(location):
    sf = SchematicFile.load(location)

    

    Y = len(sf.blocks)
    #print("Y: ", Y)
    Z = len(sf.blocks[0])
    #print("Z: ", Z)
    X = len(sf.blocks[0][0])
    #print("X: ", X)

    breakpoint
    array = np.zeros(Z*Y*X).reshape(Z, Y, X)

    for y in range(Y):
        for z in range(Z):
            for x in range(X):
                array[z,y,x] = sf.blocks[y,z,x]
    return array

def makeBlocks(input,location, Z, Y, X):
    sf = SchematicFile(shape=(Y, Z ,X))
    assert sf.blocks.shape == (Y, Z ,X)

    for y in range(Y):
        for z in range(Z):
            for x in range(X):
                sf.blocks[y,z,x] = input[z,y,x] 

    Y = len(sf.blocks)
    #print("Y: ", Y)
    Z = len(sf.blocks[0])
    #print("Z: ", Z)
    X = len(sf.blocks[0][0])
    #print("X: ", X)


    sf.save('location')