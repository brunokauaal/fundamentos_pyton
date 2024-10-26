#INPUT = ENTRADA


name = input("Qual seu nome?: ")

#Aqui precisamos tipar caso quisermos realizar uma operção matematica pois não tem como se for string

age = int(input("Qual sua idade: "))

height = float(input("Qual sua altura?: "))

#teste
age = age + 1

print("Seja bem vindo, " + name + "!"+" Sua idade é " + str(age) +" anos "+ "e você tem " + str(height) + " de altura.")


