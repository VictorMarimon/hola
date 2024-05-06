cesta = {}

productos = int(input("¿Cuantos productos desea ingresar? "))

articulo = []
precio = []

for i in range(0, productos):

    print("")
    articulos = input("Ingrese el articulo ")
    articulo.append(articulos)
    precios = int(input("Ingrese el precio "))
    precio.append(precios)

cesta["Productos"] = articulo
cesta["Precio"] = precio    

total = sum(precio)

print("")
print("Los productos son: " , cesta["Productos"])
print("El total: ", total)