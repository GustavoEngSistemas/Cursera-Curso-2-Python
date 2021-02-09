from random import randint

def lista_grande(quant):
    lista = []
    for i in range(quant):
        lista.append(randint(1, 9999))
    return lista

