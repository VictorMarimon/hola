def puede_entrar(edad = 0, nombre):
    if edad < 18:
        return "No puede entrar " 
    return "Pueden entrar "

print(puede_entrar(15, "Juan"))