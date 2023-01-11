# # Ejercicios

# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).



edad = input("Introduzca su edad: ")
int_edad = int(edad) 
cant_años = range(1,int_edad+1)

for año in cant_años:
    if año == 1:
        print (f"El usuario cumplió 1 año") 
    else: 
        print(f"El usuario cumplió {año} años")

# 2.- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
numero = input("Introduzca un número: ")
int_numero = int(numero) 
asteriscos = range(1,int_numero+1)

for asterisco in asteriscos:
    if asterisco == 1:
        print (f"*") 
    else:
        print("*" * asterisco)

    
# *
# **
# ***
# ****
# *****

# 3.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.


# 4.- Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
asignaturas_1 = float(input("Ingrese la nota obtenida en la asignatura de Matemáticas: "))
asignaturas_2 = float(input("Ingrese la nota obtenida en la asignatura de Física: "))
asignaturas_3 = float(input("Ingrese la nota obtenida en la asignatura de Arte: "))
asignaturas_4 = float(input("Ingrese la nota obtenida en la asignatura de Música: "))
asignaturas_5 = float(input("Ingrese la nota obtenida en la asignatura de Lengua: "))

asignatura = ["Matemáticas", "Física", "Arte", "Música", "Lengua"]
calificacion = [asignaturas_1,asignaturas_2,asignaturas_3,asignaturas_4,asignaturas_5]


for a,c in zip(asignatura, calificacion):
    
    print(f"Usted ha obtenido un {c} en {a}")


# 5.- Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
Introd = input("Escriba una palabra: ")

palabra = Introd

if list(palabra) == list(reversed(palabra)):
    print("Esto es un palíndromo")

else:
    print("Esto no es un palíndromo")

# 6.- Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

# 7.- Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Plátano 1400
# Manzana 2000
# Pera 	1990
# Naranja 1900


# 8.- Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


# 9.- Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra 	
# Artículo 1 	Precio
# Artículo 2 	Precio
# Artículo 3 	Precio
# … 	…
# Total 	Coste