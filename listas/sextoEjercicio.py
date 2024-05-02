# Escribir un programa que almacene el abecedario en una lista, elimine de la lista 
# las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

posiciones = []

for i in range(len(letras)):
    if(i != i*3):
        posiciones.append(i)

while True:
    print(posiciones[i])

    if(i > 24):
        break


#incompleto