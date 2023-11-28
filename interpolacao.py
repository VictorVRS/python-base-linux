
import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informe o arquivo")
    sys.exit(1)
    
filename = arguments[0] 
templatename = arguments[1]   

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


for line in open(filepath):
    name, email = line.split(",")
    print(f"Enviando o email para:{email}")
    print()
    print(
                open(templatepath).read()
                % {
                    "nome":name,
                    "produto":"Caneta",
                    "texto": "escreve muito bem",
                    "link": "https://canetaslegais.com",
                    "quantidade":1,
                    "preco" :50.5,})
    print("-" * 50)  



