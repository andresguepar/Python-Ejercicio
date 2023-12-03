print("=======Frozen Delights=======")
sabores = ["chocolate", "vainilla", "fresa", "oreo", "limon"]


conos = ["tradicional", "chocolate", "azucar"]

while True:
    sabor = input(" Escoge el sabor de helado (chocolate, vainilla, fresa, oreo, limon): ")
    if sabor in sabores:
        break
    else:
        print("El sabor no es valido")

while True:
    cono = input("Escoge el tipo de cono (tradicional, chocolate, azucar): ")
    if cono in conos:
        break
    else:
        print("El tipo de cono no es valido.")


precio = 2.50
if cono == "chocolate":
    precio += 0.50
elif cono == "azucar":
    precio += 0.25

print("=======Frozen Delights=======")
print("------Recibo--------")
print(f"Helado sabor: {sabor}")
print(f"Cono Tipo: {cono}")
print(f"El precio total es: {precio}")

