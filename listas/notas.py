colegio = []
valores = {}

while True:
    asignatura = str(input("Ingrese el nombre de la asignatura"))

    valores["asignatura"] = asignatura

    profesor = str(input("Ingrese el o los nombres de los docentes"))

    valores["Profesores"] = colegio.append(profesor)

    salon = str(input("Ingrese el nombre del salón"))

    valores["Salón"] = colegio.append(salon)

    nota = int(input("Ingrese las notas"))

    valores["Nota"] = colegio.append(nota)
    
    print("¿Desea agregar otra asignatura?")
    print("1. SI")
    print("2. NO")
    print("")
    opcion = str(input())

    if opcion == "2":
        break
    elif(opcion != "1"):
        print("Seleccione una opcion correcta")
        break

print(valores)