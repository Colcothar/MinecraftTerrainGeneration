DCGAN

convert.py - converts schematic files into numpy arrays for training
convert_back.py - converts generated images back to schematic files
dcgan - 2d.py - generates new schematic files

chunk_x.schematic - schematic files containing chunks for a flat world (they're all the same)

TODO:
  Fix problem where DCGAN is only returning values between -1 and 1 (we need 0-8 to begin with)
  
  
  ##NOTE
Numpy arrays are inedexed in the format arr[z][y][x] but schematic files are indexed sf.blocks[y,z,x], similar to in minecraft
