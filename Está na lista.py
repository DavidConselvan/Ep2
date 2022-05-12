def esta_na_lista(pais,lista):
    nova_lista = []
    i=0
    while i < len(lista):
        if pais == lista[i][0]:
            nova_lista.append(lista[i])
        i+=1
    
    if len(nova_lista) == 1:
        return True
    if len(nova_lista) == 0:
        return False