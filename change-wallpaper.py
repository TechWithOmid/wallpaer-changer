# omidmmadi@gmail.com
# Day 2 of 90coding you can follow me in instagram: @omid.mmadi

import os, random
import renameFile
from pathlib import Path

home = str(Path.home()) + '/Pictures/Walp/'

renameFile.changer() # rename the wallpapers name

images = os.listdir(os.chdir(home)) # list of wallpapers
image = random.choice(images) # chose one of wallpapers
home += image # wallpaper path
command = 'gsettings set org.gnome.desktop.background picture-uri '+ home # this command will change wallpaper

os.system(command) # change wallpaper
print(image) # print wallpaper name
