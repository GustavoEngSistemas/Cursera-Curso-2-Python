def ordena(lista):
    lista_cop = lista[:]
    fim =  len(lista)
    for i in range(fim - 1):
        pos_min = i

        for j in range(i+1, fim):
            if lista_cop[j] < lista_cop[pos_min]:
                pos_min = j

        lista_cop[i], lista_cop[pos_min] = lista_cop[pos_min], lista_cop[i]
    
    return lista_cop
