# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado 
# <nota> donde <asignatura> es cada una des las asignaturas de la lista y 
# <nota> cada una de las correspondientes notas introducidas por el usuario.

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

nota = []

for i in range(len(asignaturas)):
    notas = input("Ingrese la nota de " + asignaturas[i] + ": ")

    nota.append(notas)

print("")

for i in range(len(nota)):

    print("En " + asignaturas[i] + " has sacado: " + nota[i])