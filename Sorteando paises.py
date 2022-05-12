import random

def sorteia_pais(dicionario):
    lista_paises = []
    for paises in dicionario.keys():
        lista_paises.append(paises)
    
    pais = random.choice(lista_paises)

    return pais