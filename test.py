PALABRA = "cadena" 
PALABRA2 = 4
PALABRA3 = 2.5
PALABRA4 = ", q"
mayuscula = PALABRA[2:4].upper()
mayuscula2 = PALABRA[0:2]
mayuscula3 = PALABRA[4:]
palabra = mayuscula2 + mayuscula + mayuscula3
type1 = type(PALABRA)
type2 = type(PALABRA2)
type3 = type(PALABRA3)
print(type1)
print(type2)
print(type3)
print(palabra)