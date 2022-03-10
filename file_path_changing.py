### a code to alwys redirect files to the folder containning the same file format

import os

#source and distination directory

sorc='/home/abdo_khattab/listen/'
dist1='/home/abdo_khattab/mp3/'
dist2='/home/abdo_khattab/pic/'
dist3='/home/abdo_khattab/vid/'


## infinite loop to always redirect file 


while True:

    for file in os.listdir(sorc): ## looping throut the source directory
    
        ## check dif formats types and assigning the new path
    
        if file.endswith('.mp3'): 
            os.rename(sorc+file,dist1+file)
        elif file.endswith('.jpg'):
            os.rename(sorc+file,dist2+file)    
        elif file.endswith('.mp4') :
            os.rename(sorc+file,dist3+file)
