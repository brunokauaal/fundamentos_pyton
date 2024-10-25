# MÉTODOS UTEIS PARA STRING

name = "Bruno"

# length famoso comprimento em portugues vai imprimir o comprimento da variavel nome
print(len(name))

#So explorando descobri que semelhante ao java quando apertamos o ponto ele nos da sugestoes de metodos.
print(name.find("n"))

#Serve para deixar a primeira letra Maiscula.
print(name.capitalize())

#Deixa tudo maiusculo
print(name.upper())

#Tudo minusculo
print(name.lower())

#Se o digito for string da false caso o contrario true tipo um boolean
print(name.isdigit())

#Para checar se a string tem apenas  letras alfabeticas caso tenha numero vai dar false
print(name.isalpha())

#Contar
print(name.count("B"))

#Para substituir uma letra
print(name.replace("o", "a"))

print(name*2)