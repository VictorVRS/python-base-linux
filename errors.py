#!usr/bin/env python3
import sys
import os

#EAFP - Easy to Ask to Forgiveness than Permission

#try:
#   raise RunTimeError("Ocorreu um erro")
#   print(str{e})



try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}.") 
    sys.exit(1)   
else:
    print("Sucesso")
finally:
    print("execute isso sempre")
        

try:
    print(names[2])
except:
    print("[ERROR] Missing lines")    
    sys.exit(1)
