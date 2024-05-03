persona = {}

while True:
    nombre = str(input("Ingrese el nombre: "))
    edad = str(input("Ingrese la edad: "))
    direccion = str(input("Ingrese la direccion: "))
    telefono = str(input("Ingrese el telefono: "))
    genero = str(input("Ingrese el genero: "))
    email = str(input("Ingrese el correo: "))

    persona["Nombre"] = nombre
    persona["Edad"] = edad
    persona["Dirección"] = direccion
    persona["Telefono"] = telefono
    persona["Genero"] = genero
    persona["Email"] = email
    print("")

    print(persona["Nombre"] + " tiene " + persona["Edad"] +" años, vive en " + persona["Dirección"] +" su número de teléfono es " + persona["Telefono"]+
          " su genero es " + persona["Genero"] + " y su correo es " + persona["Email"])

    persona.clear()
    print("")
    print("¿Desea Ingresar otra persona?")
    print("1. SI")
    print("2. NO")
    opcion = int(input())
    print("")

    if(opcion != 1):
        print("")
        print("Programa finalizado")
        break