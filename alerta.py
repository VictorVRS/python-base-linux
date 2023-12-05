
"""
import sys
import logging
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None    
}
key = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"qual temp?").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)
"""

temp_atual = input("Olá!\nDigite a temperatura atual:").strip()
ind_um = input("Agora digite a umidade do ar:").strip()

if int(temp_atual) >45:
    print(f"[ALERTA!!!]Perigo Calor Extremo!")
elif int(temp_atual) > 10 and int(temp_atual) < 30:
    print(f"Temperatura Normal")
elif int(temp_atual) > 0 and int(temp_atual) < 10:
    print(f"Frio")
elif int(temp_atual) < 0:
    print(f"[ALERTA!!!]Perigo Frio Extremo!")    
else:
    int(temp_atual) * 3 >= int(ind_um)
    print(f"[ALERTA!!!]Perigo de calor umido")
    
