mes = int(input("Ingrese un número (Entre 1 y 12): -> "))

if(mes == 1):
    mes = "Enero"
elif(mes == 2):
    mes = str("Febrero")
elif(mes == 3):
    mes = str("Marzo")
elif(mes == 4):
    mes = str("Abril")
elif(mes == 5):
    mes = str("Mayo")
elif(mes == 6):
    mes = str("Junio")
elif(mes == 7):
    mes = str("Julio")
elif(mes == 8):
    mes = str("Agosto")
elif(mes == 9):
    mes = str("Septiembre")
elif(mes == 10):
    mes = str("Octubre")
elif(mes == 11):
    mes = str("Noviembre")
elif(mes == 12):
    mes = str("Diciembre")
else:
    print("Por favor ingrese un número correcto")

print(f"El mes es {mes}")
