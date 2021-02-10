def busca(lista, proc):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(meio)
        if lista[meio] == proc:
            return meio
        else:
            if proc < lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
    return False
