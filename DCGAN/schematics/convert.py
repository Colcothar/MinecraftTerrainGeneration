import numpy as np
from nbtschematic import SchematicFile
temp = np.zeros(4*4*4).reshape(4,4,4)
sf1 = SchematicFile.load('C:/Users/adamj/Documents/MinecraftTerrainGeneration/DCGAN/islands4x4/1.schematic')

for z in range(4):
    for x in range(4):
        for y in range(4):
            if int(sf1.blocks[z,y,x]) == 0:
                temp[z][y][x] = 0
            elif int(sf1.blocks[z,y,x]) == 1:
                temp[z][y][x] = 0.1
            elif int(sf1.blocks[z,y,x]) == 3:
                temp[z][y][x] = 0.3
            elif int(sf1.blocks[z,y,x]) == 2:
                temp[z][y][x] == 0.4
            elif int(sf1.blocks[z,y,x]) == 7:
                temp[z][y][x] = 0.2

schematic1 = temp

print("Before: ", temp[0][0])
print("After: ", schematic1[0][0])

temp = np.zeros(4*4*4).reshape(4,4,4)
sf2 = SchematicFile.load('C:/Users/adamj/Documents/MinecraftTerrainGeneration/DCGAN/islands4x4/2.schematic')

for z in range(4):
    for x in range(4):
        for y in range(4):
            if int(sf2.blocks[z,y,x]) == 0:
                temp[z][y][x] = 0
            elif int(sf2.blocks[z,y,x]) == 1:
                temp[z][y][x] = 0.1
            elif int(sf2.blocks[z,y,x]) == 3:
                temp[z][y][x] = 0.3
            elif int(sf2.blocks[z,y,x]) == 2:
                temp[z][y][x] == 0.4
            elif int(sf2.blocks[z,y,x]) == 7:
                temp[z][y][x] = 0.2
schematic2 = temp

temp = np.zeros(4*4*4).reshape(4,4,4)
sf3 = SchematicFile.load('C:/Users/adamj/Documents/MinecraftTerrainGeneration/DCGAN/islands4x4/3.schematic')

for z in range(4):
    for x in range(4):
        for y in range(4):
            if int(sf3.blocks[z,y,x]) == 0:
                temp[z][y][x] = 0
            elif int(sf3.blocks[z,y,x]) == 1:
                temp[z][y][x] = 0.1
            elif int(sf3.blocks[z,y,x]) == 3:
                temp[z][y][x] = 0.3
            elif int(sf3.blocks[z,y,x]) == 2:
                temp[z][y][x] == 0.4
            elif int(sf3.blocks[z,y,x]) == 7:
                temp[z][y][x] = 0.2
schematic3 = temp

temp = np.zeros(4*4*4).reshape(4,4,4)
sf4 = SchematicFile.load('C:/Users/adamj/Documents/MinecraftTerrainGeneration/DCGAN/islands4x4/4.schematic')

for z in range(4):
    for x in range(4):
        for y in range(4):
            if int(sf4.blocks[z,y,x]) == 0:
                temp[z][y][x] = 0
            elif int(sf4.blocks[z,y,x]) == 1:
                temp[z][y][x] = 0.1
            elif int(sf4.blocks[z,y,x]) == 3:
                temp[z][y][x] = 0.3
            elif int(sf4.blocks[z,y,x]) == 2:
                temp[z][y][x] == 0.4
            elif int(sf4.blocks[z,y,x]) == 7:
                temp[z][y][x] = 0.2
schematic4 = temp

temp = np.zeros(4*4*4).reshape(4,4,4)
sf5 = SchematicFile.load('C:/Users/adamj/Documents/MinecraftTerrainGeneration/DCGAN/islands4x4/5.schematic')

for z in range(4):
    for x in range(4):
        for y in range(4):
            if int(sf5.blocks[z,y,x]) == 0:
                temp[z][y][x] = 0
            elif int(sf5.blocks[z,y,x]) == 1:
                temp[z][y][x] = 0.1
            elif int(sf5.blocks[z,y,x]) == 3:
                temp[z][y][x] = 0.3
            elif int(sf5.blocks[z,y,x]) == 2:
                temp[z][y][x] == 0.4
            elif int(sf5.blocks[z,y,x]) == 7:
                temp[z][y][x] = 0.2
schematic5 = temp

temp = np.zeros(4*4*4).reshape(4,4,4)
sf6 = SchematicFile.load('C:/Users/adamj/Documents/MinecraftTerrainGeneration/DCGAN/islands4x4/6.schematic')

for z in range(4):
    for x in range(4):
        for y in range(4):
            if int(sf6.blocks[z,y,x]) == 0:
                temp[z][y][x] = 0
            elif int(sf6.blocks[z,y,x]) == 1:
                temp[z][y][x] = 0.1
            elif int(sf6.blocks[z,y,x]) == 3:
                temp[z][y][x] = 0.3
            elif int(sf6.blocks[z,y,x]) == 2:
                temp[z][y][x] == 0.4
            elif int(sf6.blocks[z,y,x]) == 7:
                temp[z][y][x] = 0.2
schematic6 = temp
'''
sf7 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk7.schematic')
temp = np.zeros(4*4*246).reshape(246,4,4)

for z in range(246):
    for x in range(4):
        for y in range(4):
            temp[z][y][x] = int(sf7.blocks[y,z,x])
temp = temp.reshape(246,246)
schematic7 = temp

sf8 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk8.schematic')
temp = np.zeros(4*4*246).reshape(246,4,4)

for z in range(246):
    for x in range(4):
        for y in range(4):
            temp[z][y][x] = int(sf8.blocks[y,z,x])
temp = temp.reshape(246,246)
schematic8 = temp

sf9 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk9.schematic')
temp = np.zeros(4*4*246).reshape(246,4,4)

for z in range(246):
    for x in range(4):
        for y in range(4):
            temp[z][y][x] = int(sf9.blocks[y,z,x])
temp = temp.reshape(246,246)
schematic9 = temp

sf10 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk10.schematic')
temp = np.zeros(4*4*246).reshape(246,4,4)

for z in range(246):
    for x in range(4):
        for y in range(4):
            temp[z][y][x] = int(sf10.blocks[y,z,x])
temp = temp.reshape(246,246)
schematic10 = temp
'''



schematics = np.stack((schematic1, schematic2, schematic3, schematic4, schematic4, schematic6), 0)

np.save('islands4x4-new.npy', schematics)
'''
print(basic.shape)
np.save('basic_air3d.npy', basic)
'''