import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Ingrese la longitud de tu contraseña"))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)
print(f"Tu contraseña con longitud {longitud} es {contraseña}")
