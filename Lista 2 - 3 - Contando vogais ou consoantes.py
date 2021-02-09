def conta_letras(frase, contar="vogais"):
    quant_vog = quant_cons = 0
    for i in range(len(frase)):
        if frase[i].lower() in ['a', 'e', 'i', 'o', 'u']: #é vogal
            quant_vog += 1
        elif frase[i].lower() != " " and (97 <= ord(frase[i].lower()) <= 122):
            quant_cons += 1
    
    if contar == "vogais":
        return quant_vog
    elif contar == "consoantes":
        return quant_cons
    else:
        return -1

