def primeiro_lex(lista):
    prim = lista[0]
    for item in lista:
        if item < prim:
            prim = item
    
    return prim
