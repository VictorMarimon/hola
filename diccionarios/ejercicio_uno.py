divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
bandera = 0
divisa_usuario = str(input("Ingrese la divisa: "))
for i in divisas:
    if(divisa_usuario == i):
        print("La divisa es: " + divisas[i])
        bandera = 1

if(bandera == 0):
    print("La divisa no existe")