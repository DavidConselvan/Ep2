import random

def sorteia_letra(string,lista):
    carac_esp = ['.', ',', '-', ';', ' ']
    lista_sorteavel = [] 
    lista_restrita = []
    
    for letra in lista:
        lista_restrita.append(letra)
        if letra.lower() == letra:
            lista_restrita.append(letra.upper())
        else:
            lista_restrita.append(letra.lower())

    print(lista_restrita)
        
    for caractere in string:
        if caractere not in lista_restrita and caractere not in carac_esp:
            lista_sorteavel.append(caractere)

    if len(lista_sorteavel) == 0:
        return ''

    sorteio = random.choice(lista_sorteavel)

    return sorteio

print(sorteia_letra('Andorra a-Velha',['a', 'r']))