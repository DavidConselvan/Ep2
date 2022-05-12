def normaliza(dicionario):
    new_dic = {}
    for cont,info in dicionario.items():
        for chaves, dados in info.items():
            new_dic[chaves] = dados        
    return new_dic