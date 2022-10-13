# Vamos a repasar primero la operatoria entre int y string
int_1 = 1
int_2 = 2
# el operador + entre integers es la suma
suma_ints = int_1 + int_2
# usamos print con un f string (f"") para poder usar variables dentro
print(f"la suma de integers es: {suma_ints}")
# en este contexto, int_1 y int_2 no fueron modificados, solo suma_ints tiene el valor de la suma

string_1 = "Hola "
string_2 = "Github "
# el operador + entre strings es la concatenación (añadir un string al final de otro string)
suma_strings = string_1 + string_2
# suma_strings retorna "Hola Github"
print(f"la concatenación de strings es: {suma_strings}")
# en este contexto, string_1 y string_2 no fueron modificados, solo suma_strings tiene el valor de la concatenación

# cómo pasamos un int a string?
string_1 = str(int_1)
string_2 = str(int_2)
# el operador + entre strings es la concatenación (añadir un string al final de otro string)
suma_strings = string_1 + string_2
# suma_strings retorna el string "12"
print(f"la concatenación de strings es: {suma_strings}")

# cómo pasamos un string a integer?
int_3 = int(suma_strings)
# retorna el integer 12
multiplicacion = int_3 * 3
# retorna la multiplicación es 12 * 3 = 36
print(f"la multiplicación de integers es: {multiplicacion}")

# si cambiamos el valor de una variable, no afectamos las otras variables
int_1 = 50
print(f"el valor de int_1 es {int_1}")
print(f"el valor de int_2 siempre fue {int_2}")
print(f"el valor de multiplicacion siempre fue {multiplicacion}")

# Ahora vamos a ver los if y else
# if funciona con un argumento que va a ser un boolean
# boolean = True o False, no hay un entremedio
verdad = True
if verdad:
    print(f"Esto es Verdad, verdad es {verdad}")

# los boolean también se pueden negar
mentira = False
if not mentira:
    print(f"Esto no es mentira, mentira es {mentira}")

# si quiero comparar 2 integers la lógica sería
if int_1 == 1:
    # int_1 == 1 significa que compara el valor de la variable 'int_1' y lo compara con el integer 1. Si esto es
    # verdadero ejecuta el bloque correspondiente
    print("El int_1 es igual a 1 (como integer)")
if int_1 == "1":
    # int_1 == 1 significa que compara el valor de la variable 'int_1' y lo compara con el string 1. Si esto es
    # verdadero ejecuta el bloque correspondiente, pero en este caso, se ejecuta else dado que int_1 no es string
    print("Cuidado con esto !!! ")
else:
    # aqui queda el bloque que se ejecutaría en el caso de que la afirmación del if sea False
    print("El int_1 no es igual a '1' puesto que no es un string")

# si quiero comparar 2 strings la lógica sería
if string_1 == "perro":
    print("guau")
else:
    print("el string_1 no es un perro")

# Listas
# las listas son estructuras que permiten enlazar datos, estos datos pueden ser de cualquier tipo.
lista_integers = [1, 2, 3]
lista_strings = ["a", "b", "c"]
print(f"la lista de integers es: {lista_integers}")
print(f"la lista de strings es: {lista_strings}")

# las listas incluso podrían llegar a tener cosas de distinto tipo, pero no es recomendable
lista_mixta = ["12345", 3344, "guau"]
print(f"la lista mixta es: {lista_mixta}")

# para acceder a cosas de la lista se usa lista[n], donde n es un número que va de 0 al tamaño de la lista
print(lista_mixta[0])
print(lista_mixta[2])

# para saber el tamaño de una lista se usa len(lista), retorna un integer
lista_length = len(lista_mixta)
print(f"el tamaño de la lista_mixta es {lista_length}")


# Diccionarios
# los diccionarios son elementos que obedecen la regla {llave: valor}
# de esta manera podemos almacenar distinta información en un diccionario, incluso agregarle o quitarle elementos
# la llave se recomienda que sea un string y el valor puede ser lo que quieras (una lista, otro diccionario, int, etc)
diccionario_fecha = {"año": 2022, "mes": "Julio", "día": 13}
# accedemos a los elementos del diccionario llamando por su llave
cum = (
    str(diccionario_fecha["día"])
    + " de "
    + diccionario_fecha["mes"]
    + " del año "
    + str(diccionario_fecha["año"])
)
print(f"El cumpleaños del profe es {cum}")

# Listas de diccionario:
# las listas tambien pueden contener diccionarios, como en el ejemplo del escrito japonés
escritura1 = {
    "palabra": "かさ",
    "significado": "paraguas",
    "silabario": "hiragana",
    "origen": "Japón",
}
escritura2 = {
    "palabra": "ケーキ",
    "significado": "torta",
    "silabario": "katakana",
    "origen": "Japón",
}
escritura3 = {
    "palabra": "本",
    "significado": "libro",
    "silabario": "kanji",
    "origen": "China",
}
escritura4 = {
    "palabra": "日",
    "significado": "día",
    "silabario": "kanji",
    "origen": "China",
}

lista_escrituras = [escritura1, escritura2, escritura3, escritura4]

# Iteraciones (for)
# se puede iterar sobre un string, una lista o un diccionario.
# lo que esté dentro del bloque del for se ejecutará por cada valor que tome por la iteración
saludo_hola = "Hola"
# iterar sobre un string
for letra in saludo_hola:
    print(letra)
# esto va a imprimir H, o, l, a

# iterar sobre una lista
for escritura in lista_escrituras:
    palabra = escritura["palabra"]
    significado = escritura["significado"]
    print(f"la palabra {palabra} significa {significado}")
# esto va a iterar sobre las 4 escrituras

# iterar sobre un diccionario
# esta iteración itera sobre las llaves del diccionario (no sus valores)
for llave in escritura1:
    valor = escritura1[llave]
    print(f"la llave es {llave}, el valor es {valor}")

# funciones
# para llamar a una función se requiere usar la sintaxis "funcion()"
# si es que la función recibe uno o más argumentos sería funcion(arg1, arg2....)
# la función print puede recibir más argumentos pero por ahora usamos solamente 1 argumento el cual sería un string
print("Este es el string que recibe la función print")
# también hay otras funciones que retornan distintas cosas, en python docs hay miles de funciones
# que vienen incluídas en la biblioteca estándar
# la gracia de las funciones es que nosotros podemos crearlas con lo que queramos!
def saludar_persona(persona):
    return f"Hola {persona}"


# la funcion saludar_persona recibe el  string persona como argumento y retorna "Hola " + el nombre de la persona.
print(saludar_persona("Alumno/a/e"))


def sumar_numeros(numero1, numero2):
    return numero1 + numero2


print(sumar_numeros(10, 20))
# la funcion sumar_numeros retorna la suma de los 2 numeros, ojo que en este caso no estamos validando que sean ints
# de este modo esta funcion podría incluso concatenar strings
print(sumar_numeros("Hola", "12345"))

# los retornos de las funciones se pueden almacenar en una variable, lo cual resulta muy útil para operarlas.

saludo = saludar_persona("persona")
saludo_nuevo = saludo + "~desu"
print(f"Cómo quisiera decirte: {saludo_nuevo}")
