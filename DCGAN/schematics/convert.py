import numpy as np
from nbtschematic import SchematicFile
temp = np.zeros(16*16*8).reshape(8,16,16)
sf1 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk1.schematic')

for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf1.blocks[z,x,y] / 10
            print(sf1.blocks[z,x,y] / 10)

temp = temp.reshape(8,256)

schematic1 = temp

sf2 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk2.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf2.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic2 = temp

sf3 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk3.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf3.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic3 = temp

sf4 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk4.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf4.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic4 = temp

sf5 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk5.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf5.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic5 = temp

sf6 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk6.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf6.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic6 = temp

sf7 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk7.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf7.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic7 = temp

sf8 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk8.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf8.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic8 = temp

sf9 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk9.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf9.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic9 = temp

sf10 = SchematicFile.load('C:/Users/adamj/Documents/Minecraft/GAN/DCGAN/schematics/chunk10.schematic')
temp = np.zeros(16*16*8).reshape(8,16,16)
for z in range(8):
    for x in range(16):
        for y in range(16):
            temp[z][x][y] = sf10.blocks[z,x,y] / 10
temp = temp.reshape(8,256)
schematic10 = temp




schematics = np.stack((schematic1, schematic2, schematic3), 0)

np.save('schematics.npy', schematics)