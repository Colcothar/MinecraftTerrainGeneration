import numpy as np
from nbtschematic import SchematicFile

sf = SchematicFile(shape=(8, 16, 16))

genSF = np.load("C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/arrays/mnist_100.npy")
print(genSF.shape)
genSF = genSF[0]
genSF = genSF.reshape(8, 16, 16)

for z in range(8):
    for x in range(16):
        for y in range(16):
            sf.blocks[z,x,y] = int(np.round(int(genSF[z][x][y]*10)))
            #print(int(np.round(int(genSF[z][x][y]))))
            #if int(np.round(int(genSF[z][x][y]))) != 0:
            if genSF[z][x][y] != 0:
                print(int(np.round(genSF[z][x][y])))

                print(genSF[z][x][y])
            
sf.save('mnist_250.schematic')