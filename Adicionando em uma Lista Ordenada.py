def adiciona_em_ordem(pais,distancia,lista):
    nova_lista = []

    if len(lista) == 0:
        nova_lista.append([pais, distancia])

    c=0
    while c < len(lista):
        
        if lista[c][1] < distancia:
            nova_lista.append(lista[c])

        if lista[c][1] >= distancia:
            if pais == lista[c][0]:
                nova_lista.append(lista[c])
                c+=1
            else:
                nova_lista.append([pais, distancia])
            break  
        
        c+=1
        
    print(c)

    while c < len(lista):
        nova_lista.append(lista[c])
        c+=1
    
    return nova_lista

pais = 'siria'
distancia = 5919
lista = [
    ['libia', 3678],
    ['franca', 3998],
    ['egito', 5008],
    ['india', 9919],
    ['japao', 13836]
]

print(adiciona_em_ordem(pais,distancia,lista))