def soma_matrizes(m1, m2):
    
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        matriz_soma = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                linha.append(m1[i][j] + m2[i][j])
            matriz_soma.append(linha)
        return matriz_soma
    else:
        return False


