Empresas = {

"Empresa 1": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 4}, {"departamento": "Ventas", "empleados": 10}, {"departamento": "Operaciones", "empleados": 25}],

"Empresa 2": [{"departamento": "Recursos Humanos", "empleados": 11}, {"departamento": "Contabilidad", "empleados": 15}, {"departamento": "Ventas", "empleados": 25}, {"departamento": "Operaciones", "empleados": 41}],

"Empresa 3": [{"departamento": "Recursos Humanos", "empleados": 8}, {"departamento": "Contabilidad", "empleados": 20}, {"departamento": "Ventas", "empleados": 32}, {"departamento": "Operaciones", "empleados": 56}],

"Empresa 4": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 8}, {"departamento": "Ventas", "empleados": 15}, {"departamento": "Operaciones", "empleados": 29}],

"Empresa 5": [{"departamento": "Recursos Humanos", "empleados": 20}, {"departamento": "Contabilidad", "empleados": 35}, {"departamento": "Ventas", "empleados": 58}, {"departamento": "Operaciones", "empleados": 97}],

}

def diez_empleados(empresa):

    contador_empresas = 0

    for i, j in empresa.items():
        contenido = j
        for k in contenido:
            recurso = k["departamento"]
            if(int(k["empleados"]) > 10 and recurso == "Recursos Humanos"):
                contador_empresas += 1
    print("Empresas tienen más de 10 empleados en Recursos Humanos son: ", contador_empresas)

def promedio_empleados(empresa):

    promedio = {}
    empleados_totales = 0

    for i,j in empresa.items():
        contenido = j
        for l in range(0, len(contenido)):
            promedio[j[l]["departamento"]] = "Hola"
            while(promedio["Recursos Humanos"]):
                empleados_totales += j[l]["empleados"]
                promedio[j[l]["departamento"]] = empleados_totales
                break
            #for k in contenido:
                #print(k)
                #print("departamentos",k["departamento"])
                #print(k["empleados"])
    for llave,valor in promedio.items():
        print(llave, valor)

                


promedio_empleados(Empresas)
#diez_empleados(Empresas)
