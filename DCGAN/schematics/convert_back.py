import numpy as np
from nbtschematic import SchematicFile

sf = SchematicFile(shape=(4, 4, 4))

genSF = np.load("C:/Users/adamj/Documents/MinecraftTerrainGeneration/DCGAN/arrays/mnist_1362.npy")
print(genSF.shape)
genSF = genSF[0]
genSF = genSF.reshape(4, 4, 4)
new = np.arange(64).reshape(4,4,4)
print(genSF[0,0,0])
print(type(genSF[0,0,0]))
#sf.blocks = genSF * 10
print(genSF)
for z in range(4):
    for x in range(4):
        for y in range(4):
            print(int(np.round(genSF[z][y][x]*10)))
            print(type(int(np.round(genSF[z][y][x]*10))))
            #print(type(genSF[z][y][x]*10))
            #print(int(np.round(genSF[z][y][x]*10)))
            if int(np.round(genSF[z][y][x]*10)) < 0:
                genSF[z][y][x] = int(np.round(genSF[z][y][x]*10)*-1)
                #print(genSF[z][y][x])
                
            if (int(np.round(genSF[z][y][x]*10))) == 0:
                print(int(np.round(genSF[z][y][x]*10)))
                print(type(int(np.round(genSF[z][y][x]*10))))
                new[z][y][x] = 0
            elif (int(np.round(genSF[z][y][x]*10))) == 1:
                new[z][y][x] = 1
            elif (int(np.round(genSF[z][y][x]*10))) == 3:
                new[z][y][x] = 3
            elif (int(np.round(genSF[z][y][x]*10))) >= 4:
                new[z][y][x] == 2
            elif (int(np.round(genSF[z][y][x]*10))) == 2:
                new[z][y][x] = 7
            
            #print(int(np.round(int(genSF[z][x][y]*10))))
            #if int(np.round(int(genSF[z][x][y]*10))) < 0:
                #sf.blocks[z,x,y] = int(np.round(int(genSF[z][x][y]*10)))*-1
                
            #if int(np.round(int(genSF[z][x][y]*10))) != 0:
                #print(sf.blocks[z,x,y])

print(new)
sf.blocks = new
print(sf.blocks)
sf.save('mnist_1362-3d.schematic')