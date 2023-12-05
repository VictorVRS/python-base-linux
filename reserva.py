
import sys
import logging


RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

ocupados = {}
try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome_cliente": nome_cliente,
            "dias": int(dias)}
except FileNotFoundError:
    logging.error("Arquivo não existe",QUARTO_FILE)
    sys.exit(1)
            
quartos = {}
try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(",")
        quartos[int(num_quarto)] = {
            "nome_quarto": nome_quarto,
            "preco": float(preco),
            "disponivel": False if int(num_quarto) in ocupados else True
            }
except FileNotFoundError:
    logging.error("Arquivo não existe",QUARTO_FILE)
    sys.exit(1)    

print("Reservas do Hotel")
print("-" * 55)
if len(ocupados)  == len(quartos):
    print("Hotel Lotado!")
    sys.exit(0)

nome_cliente = input("Qual o seu nome:").strip()
print()
head = ["Número", "Nome do Quarto", "Preço", "Disponível"]
print("lista de Quartos")
print()
print(f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")
        
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "Não há Vagas" if not dados_quarto["disponivel"] else "Há Vagas"
    print(f"{num_quarto:<6} - {nome_quarto:<14} - R$ {preco:<9.2f} - {disponivel:<10}")

print("-" * 55)
try:

    num_quarto = int(input("Qual o número do quarto desejado? ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"Quarto {num_quarto} Indisponivel")  
        sys.exit(0)
except KeyError:
    print("Quarto Inexistente")
    sys.exit(0)     
except ValueError:
    print("Numero Inválido! Digite apenas números")
    sys.exit(0)   

try:

    dias = int(input("Quantos dias deseja para sua estadia? ").strip())
except ValueError:
    print("Numero Inválido! Digite apenas números")
    sys.exit(0)  
              
nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_diaria = quartos[num_quarto]["preco"]
total = dias * preco_diaria

print(
    f"Olá {nome_cliente}, você escolheu  {nome_quarto} "
    f"o valor total estimado será R$ {total:.2f}"   
)
if input("Confirma? [digite y]").strip().lower() in ("y", "yes", "sim","s"):
    with open(RESERVAS_FILE, "a") as reserva_file:
        reserva_file.write(f"{nome_cliente}, {num_quarto}, {dias}\n")
