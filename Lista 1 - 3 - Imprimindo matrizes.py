def imprime_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if j != colunas - 1:
                print(f"{matriz[i][j]}", end=' ')
            else:
                print(f"{matriz[i][j]}")



minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)


