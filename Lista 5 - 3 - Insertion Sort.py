def insertion_sort(lista):
    lista_ord = [lista[0]]
    for i in range(1, len(lista)):
        inseriu = False
        for j in range(len(lista_ord)):
            if lista[i] < lista_ord[j]:
                lista_ord.insert(j, lista[i])
                inseriu = True
                break
        if not inseriu:
            lista_ord.append(lista[i])
    return lista_ord

