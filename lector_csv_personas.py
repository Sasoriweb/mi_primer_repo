import csv

# creamos una lista vacía para almacenar información sobre personas
personas = []

# leemos el archivo CSV y agregamos cada persona a la lista
with open("personas.csv", mode="r") as archivo_csv:
    reader = csv.DictReader(archivo_csv)
    for row in reader:
        personas.append(row)

# mostramos la información de cada persona en la lista
for persona in personas:
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    print("Sexo:", persona["sexo"])
    print("Teléfono:", persona["telefono"])
    print("Correo electrónico:", persona["correo"])
    print()
