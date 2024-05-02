
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine 
# de la lista las asignaturas aprobadas. Al final el programa debe mostrar 
# por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

tamanio = len(asignaturas)
posiciones = []

for i in range(tamanio):

    nota = float(input("Ingrese la nota que saco en " + asignaturas[i] + ": "))

    if nota < 3:
        posiciones.append(i)

print("")
print("De repetir: ")
print("")

for i in posiciones:
    print(asignaturas[i])