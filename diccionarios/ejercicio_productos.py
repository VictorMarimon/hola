productos = {"Productos": ["arroz", "maiz", "pera"], 
             "Precio": [1000,200,3300]}

nombre_producto = str(input("Ingrese el nombre del producto: "))
corte = 0
producto = productos.get("Productos")

for i in range(len(list(producto))):
    
    valor_producto = productos["Productos"][i]
    
    if(nombre_producto == valor_producto):
        precio = productos["Precio"][i]

        print("El producto es: ")
        print(valor_producto)
        print("El precio es: ")
        print(precio)
        corte = 1

if(corte == 0):
    print("El producto no existe")


    
    
        
