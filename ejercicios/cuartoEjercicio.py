edad = 16
sueldo = 1000

edadIngresada = int(input("Ingrese su edad: "))
sueldoIngresado = int(input("Ingrese su sueldo: "))

if not(edadIngresada > edad):
    input(f"No puede tributar debido a la edad {edadIngresada}")
elif not(sueldoIngresado > sueldo):
    input(f"No puede tributar debido al sueldo {sueldoIngresado}")
else:
    input("")
    input("Si puede tributar")