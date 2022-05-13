def adiciona_em_ordem(pais,dist,lista):
    novo_pais = [pais,dist]
    nova_lista = []

    if pais in lista:
        return lista
    
    i = 0
    j= 0

    while i<len(lista):
        if novo_pais[1]< lista[i][1] and j == 0:
            nova_lista.append(novo_pais)
            j= 1
        else:
            nova_lista.append(lista[i])
            i+=1
    if j == 0:
        nova_lista.append(novo_pais)
    return nova_lista