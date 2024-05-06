factura_sin_pagar = {"Factura": [],
                       "Costo": []}

factura_pagada = {"Factura": [],
                    "Costo": []}

def agregarFactura(factura):

    print("")
    id = input("Ingrese el ID de la factura ")
    dinero = int(input("Ingrese el costo "))
    print("")
    
    factura["Factura"].append([id])
    factura["Costo"].append([dinero])


def pagarFactura(factura_deuda, factura_pago):
    print("")
    id = input("Ingrese el ID de la factura ")

    factura_pendiente = factura_deuda["Factura"]

    for i in factura_pendiente:
        if(i == id):
            indice_factura = factura_pago["Factura"].index(i)
            factura_pago["Factura"].append([i])
            dinero_factura = factura_pago["Costo": [indice_factura]]   
            factura_pago["Costo"].append([dinero_factura]) 

print("Bienvenido a gestion de facturas")
print("¿Que desea realizar?")

while True:
    
    print("¿Desea realizar otra acción?")
    print("1. Agregar una factura")
    print("2. Pagar una factura")
    print("3. Ninguna de las anteriores")
    opcion = input()

    if(opcion == "3"):
        print("Programa finalizado")
        print("")
        break
    elif(opcion == "1"):
        agregarFactura(factura_sin_pagar)
    elif(opcion == "2"):
        pagarFactura(factura_sin_pagar, factura_pagada)
    else:
        print("")
        print("Seleccione una opción correcta")
        print("")

cantidad_pendiente = []
dinero_pendiente = factura_sin_pagar["Costo"]

cantidad_pagada= []
dinero_pagado = factura_pagada["Costo"]

for i in dinero_pendiente:
    cantidad_pendiente.extend(i)

for i in dinero_pagado:
    cantidad_pagada.extend(i)

print("")
print("Cantidad pendiente: ", sum(cantidad_pagada))
print("Cantidad pendiente: ", sum(cantidad_pendiente))