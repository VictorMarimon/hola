verduras = {"Brócoli": 2500,
            "Pimentón": 1250,
            "Arveja": 3500}

punto = 0

verdura = input("Ingrese el nombre del vegetal: ")

for i in verduras:
    if(verdura == i):
        punto = 1
        if(i == "Brócoli"):
            kilos = int(input("Ingrese la cantidad de kilos: "))
            print("El total a pagar es: ")
            print("$" , verduras[i] * kilos)
            break
        elif(i == "Pimentón"):
            kilos = int(input("Ingrese la cantidad de kilos: "))
            print("El total a pagar es: ")
            print("$" , verduras[i] * kilos)
            break
        elif(i == "Arveja"):
            kilos = int(input("Ingrese la cantidad de kilos: "))
            print("El total a pagar es: ")
            print("$" , verduras[i] * kilos)
            break
if(punto == 0):
    print("La verdura no existe")