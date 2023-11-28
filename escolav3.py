#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ ="0.3.1"

escola = {
        "sala1":("Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"),
        "sala2":("joao", "Maria", "Moana", "Carlos", "Antonio")
}
#sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
#sala2 = ["joao", "Maria", "Joana", "Carlos", "Antonio"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Moana", "Antonio"]

atividades = [
    ("Ingles", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]


for nome_atividade,  atividade in atividades:

    print(f"Aula de {nome_atividade}")
    print()
    atividade_sala1 = set(escola["sala1"]) & set(atividade)
    atividade_sala2 = set(escola["sala2"]) & set(atividade) 
   # atividade_sala1 = set(sala1) & set(atividade)
   # atividade_sala2 = set(sala2) & set(atividade)


    print(f"{nome_atividade} Sala 1", atividade_sala1)
    print(f"{nome_atividade} Sala 2", atividade_sala2) 
    print("-" * 30)           
