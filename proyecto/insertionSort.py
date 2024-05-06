cartas = [8, 5, 2, 10, 6, 9, 3, 4, 7, 1]

print("Cartas desordenadas: ", cartas)

for i in range(1, len(cartas)):
    comparacion = cartas[i]

    j = i - 1

    while j >= 0 and comparacion < cartas[j]:
        cartas[j + 1] = cartas[j]

        j -= 1
    cartas[j + 1] = comparacion

print("Cartas ordenadas: ", cartas)