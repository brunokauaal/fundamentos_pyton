# if statements = declarações if = um bloco de código que será executado se sua codificação for verdadeira


age = int(input("Quantos anos você tem?: "))



#Se idade for maior ou igual a 60 exiba o print muito semelhante ao java obs: se a indentação nao estiver correta nao funfa

if age >= 60 and age <= 99:
    print("Você é um idoso(a)!")

#elif seria uma abreviação de else e if = senão se

elif age >= 100 :
    print("Você  é uma lenda!")


elif age >=18 :
    print("Você ja é um adulto!")

elif age < 0 :
    print("Você ainda não nasceu!")

else:
    print("Você é uma criança!")