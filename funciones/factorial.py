def factorial(num):
    resul = 1
    for i in range(1, num+1):
        resul = i * resul
    
    print(resul)

num = int(input("Ingrese un número "))

factorial(num)