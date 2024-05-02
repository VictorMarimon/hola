num1 = int(input("Ingrese el dividendo: "))
num2 = int(input("Ingrese el divisor: "))



while(True):
    if(num2 == 0):
        num2 = int(input("El divisor debe ser mayor a cero: "))
    else:
        div = num1 / num2
        print("")
        print(f"La division el igual a {div}")
        print("")
        break