import random

def sorteia_letra(string,lista):

    lista_sorteavel = [] 
    for caractere in string:
        if caractere not in lista:
            lista_sorteavel.append(caractere)

    if len(lista_sorteavel) == 0:
        return ''

    sorteio = random.choice(lista_sorteavel)

    return sorteio