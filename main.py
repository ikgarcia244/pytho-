import random

caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Introduce la longitud de la contraseña: "))

contraseña = ""

for i in range(longitud):
    simbolo = random.choice(caracteres)
    contraseña += simbolo

print("La contaseña generada es:", contraseña)
