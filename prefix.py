#!/usr/bin/env python3








import os
import sys
from datetime import datetime
import logging
from logging import handlers
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("victor", log_level)
fh = handlers.RotatingFileHandler(
    "logprefix.log",
    maxBytes=500, #10**6
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

fh.setFormatter(fmt)
log.addHandler(fh)

arguments = sys.argv[1:]

if not arguments:
    operation = input("operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
    
elif len(arguments)!=3:
    print("numero Inválido")
    print("soma 5 5")
    sys.exit(1)
    
operation, *nums = arguments

valid_operation = {"sum", "sub", "mul", "div"}
if operation not  in valid_operation:
    print("operação Inválida")
    print(valid_operation)
    sys.exit

validated_nums = []
for num in nums:
    if not num.replace(".","").isdigit():
        print(f"NUmero inválido{num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
try:        
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)    

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2   
elif operation == "div":
    result = n1 / n2

path = "/"
filepath = os.path.join(path,"prefix.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

print(f"O resultado é {result}:")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
except PermissionError as e:
    log.error(str(e))
    sys.exit(1)



    
   
            
        
    
    
    

