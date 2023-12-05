#!/usr/bin/env python3

"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text: 
Anotação Geral sobre carreira

$notes.py read --tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]


if not arguments:
    print("invalid")
    sys.exit(1)


    if arguments[0] not in cmds:
        print(f"invalid command{arguments[0]}")
while True:
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual é a tag?").strip().lower()      
        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"title:{title}"),
                print(f"tag:{text}"),
                print("-" * 30),
                print()
                sys.exit(0)        
          
    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("Digite o Título:").strip().title()
                
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:").strip(),]
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
    usercheck = input("Deseja continuar [N,y]").strip().lower()
    if usercheck != "y":
        break
   
    
                  
       
