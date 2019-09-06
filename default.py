#!/usr/bin/python3

import os
import shutil

mydir = os.getcwd()
mydirContents = os.listdir(mydir)
base = '/mnt'

print("my current working directory is: " + mydir)
print("this is what is in that directory: ")
print(mydirContents)

#os.makedirs("arms/and/legs")

for dir_path, dir_names, file_names in os.walk(mydir):
    for f in file_names:
        print(f)
