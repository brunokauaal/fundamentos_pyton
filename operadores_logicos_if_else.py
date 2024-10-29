#Operadores lógicos (e,ou,não) = usados para verificar se duas ou mais declarações de condição


temp = int(input("Como esta a temperatura la fora hoje?: "))


if temp >= 0 and temp <= 30:
    print("A temperatura esta boa hoje!")
    print("Vai pra fora!!!")
elif temp < 0 or temp > 30:
    print("Melhor ficar em casa hoje!")
    print("Fique dentro de casa!")