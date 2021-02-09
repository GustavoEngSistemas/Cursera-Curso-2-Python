def dimensoes(matriz):
    i = j = 0
    for linha in matriz:
        if i == 0:
            for coluna in linha:
                j += 1
        i += 1

    print(f"{i}X{j}")


minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
