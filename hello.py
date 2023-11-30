#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.
Como usar:

Tenha a variável Lang devidamente configurada ex:

     export LANG=pt_BR

Execução:

     python3 hello.py
     ou
     ./hello.py
"""
__version__= "0.1.3"
__author__ = "Victor Rodrigo"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("victor", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You use %s to split"
            "You need use '=' to split key and value",
            arg,
            str(e)
            )
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value    
    

current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else: 
        current_language = input("Choose a language:")


current_language = current_language[:5]    
    
msg = {
    "en_US":"Hello, World!",
    "pt_BR":"Olá,Mundo!",
    "it_IT":"Ciao,Mondo!",
    "es_SP":"Hola, Mundo!",
    "fr_FR":"Bonjour, Monde!",}

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR]{str(e)}")
    print(f"[ERROR] Invalid language!\n")
    print(f"Please choose a Language:{list(msg.keys())}")    
    sys.exit(1)

print(msg[current_language] * int(arguments["count"]))        

#if current_language == "pt_BR":
   # msg = "Olá, Mundo!"
#elif current_language == "it_IT":
   # msg = "Ciao, Mondo!"    
#elif current_language == "es_SP":
   # msg = "Hola, Mundo!"
#elif current_language == "fr_FR":
   # msg = "Bonjour, Monde!"    



