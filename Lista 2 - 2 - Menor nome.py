def menor_nome(nomes):
    menor = nomes[0].strip()
    quant_menor = len(menor)
    for nome in nomes:
        nome = nome.strip()
        
        if len(nome) < quant_menor:
            menor = nome
            quant_menor = len(nome)
    return menor.capitalize()

