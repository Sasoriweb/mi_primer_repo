import csv

# creamos una lista vacía para almacenar información sobre personas
personas = []


while True:
    # solicitamos la información sobre la persona
    nombre = input("Introduce el nombre de la persona: ")
    edad = input("Introduce la edad de la persona: ")
    sexo = input("Introduce el sexo de la persona: ")
    telefono = input("Introduce el teléfono de la persona: ")
    correo = input("Introduce el correo electrónico de la persona: ")

    # creamos un diccionario con la información de la persona
    persona = {
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "telefono": telefono,
        "correo": correo,
    }

    # agregamos el diccionario a la lista de personas
    personas.append(persona)

    # preguntamos al usuario si quiere agregar más información
    respuesta = input("¿Desea agregar más información? (S/N)")

    # si la respuesta es "N", salimos del bucle
    if respuesta.upper() == "N":
        break

# guardamos la lista de personas en un archivo CSV
with open("personas.csv", mode="w", newline="") as archivo_csv:
    campos = ["nombre", "edad", "sexo", "telefono", "correo"]
    writer = csv.DictWriter(archivo_csv, fieldnames=campos)
    writer.writeheader()
    for persona in personas:
        writer.writerow(persona)
