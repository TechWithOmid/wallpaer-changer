# omidmmadi@gmail.com
# Day 2 of 90coding you can follow me in instagram: @omid.mmadi

import os
from pathlib import Path


home = str(Path.home()) + '/Pictures/Walp/'
count = 0

def changer():
    global count
    for image in os.listdir(home):
        if image == 'script.py':
            continue
        count = count + 1
        newName = f"wp-{count}" 
        os.rename(image, newName)
