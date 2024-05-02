contraseña = "abc123"

contraseñaInput = input("Por favor ingrese la contraseña correcta: ")

contra = contraseñaInput.lower()
while(True):

    if(contra == contraseña):
        print(" ")
        print(f"{contraseña} es la contraseña igual que {contraseñaInput}")
        break
    else:
        contraseñaInput = input("Vuelva a ingresar la contraseña: ")

    contra = contraseñaInput.lower()    