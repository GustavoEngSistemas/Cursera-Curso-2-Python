def maiusculas(frase):
    final = ""
    for i in range(len(frase)):
        if 65 <= ord(frase[i])  <= 90:
            final += frase[i]
    return final
