#!usr/bin/env python3

import sys
import os

if os.path.exists("names.txt"):
    names = open("names.txt").readlines()
else:
    print("File not found") 
    sys.exit(1)   

if len(names) >= 3:
    print(names[2])
else:
    print("[ERROR] Missing lines")    
    sys.exit(1)
