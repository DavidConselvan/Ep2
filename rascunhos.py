if opcao == '4':
    pop_pais =  dados_normalizados[pais_aleatorio]['populacao']
    print('\nA população do país é de {}'.format(pop_pais))
    tentativas+=5
    dicas+= 'A população do país é de {}\n'.format(pop_pais)
            

if opcao == '5':
    cont_pais = dados_normalizados[pais_aleatorio]['continente']
    print('\nO continente do país é {}'.format(cont_pais))
    tentativas+=7
    dicas+= 'O continente do país é {}\n'.format(cont_pais)
    print('\nVocê ainda tem {} tentativas'.format(20-tentativas))  