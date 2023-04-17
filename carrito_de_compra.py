import json

# Intentamos abrir el archivo json si existe, si no, lo creamos vacío
try:
    with open("carrito.json", "r") as archivo:
        cesta = json.load(archivo)
except FileNotFoundError:
    cesta = {}

# Pedimos al usuario que introduzca los artículos y sus precios
while True:
    articulo = input("Introduce un artículo (o pulsa Enter para terminar): ")
    if not articulo:
        break
    precio = int(input("Introduce el precio de {} en pesos chilenos: ".format(articulo)))
    cesta[articulo] = precio

# Guardamos los datos en el archivo json con pretty print
with open("carrito.json", "w") as archivo:
    json.dump(cesta, archivo, indent=4)

# Mostramos la lista de la compra y el coste total
print("\nLista de la compra")
total = 0
for articulo, precio in cesta.items():
    if len(articulo) > 20:
        articulo = articulo[:15] + "~" + articulo[-4:]
    print("{:<20} {}{:>6}".format(articulo, "$", precio))
    total += precio
print("-" * 30)
print("{:<20} {}{:>6}".format("Total", "$", total))
