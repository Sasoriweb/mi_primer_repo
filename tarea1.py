# tarea para yolanda

# Repaso
# lista_integers = range(32)
# for i in lista_integers:
#     print("niño tiene " + str(i) + "años ")
#     if i < 18:
#         print("es menor de edad")
#     else:
#         print("es mayor de edad")



# for c in "Yolanda tiene pocas dudas, me da un poco de miedo":
#     print(c)

# # tomar un input del usuario (string) y convertirlo a integer (int)
# celcius = int(input("Temp. in Celcius: "))
# # la formula de farenheit es (celcius * 9)/ 5 + 32, celcius es un integer
# farenheit = celcius*9/5 + 32
# # imprimimos como string el restultado del integer farenheit
# print("Farenheit = " + str(farenheit))


# # tomar un input del usuario (string) y convertirlo a integer (int)
# ovejas = int(input("Contemos ovejas: "))
# # listado_ovejas = range(1,ovejas+1)
# listado_ovejas = range(ovejas)
# for oveja in listado_ovejas:
#     print("Cuento " + str(oveja+1) + " Ovejas")


"""
Tarea:
Iterar sobre una lista de fechas:
Pero no cualquier fecha.
Fechas en japonés
"""
dias = range(1,32) # esto va a ser un listado de integers (del 1 al 31)
meses = range(1,13) #esto va a ser un listado de integers (del 1 al 12)


# implementar un listado de fechas en japonés
# utilizando dias y meses
kanji_gatsu = " gatsu "
kanji_nichi = " nichi "
for mes in meses:
    for dia in dias:
        # concatenar strings
        print("a")


# bonus:
# si los dias en japones ocupan una y en su nombre real (yokka)
# concatenar el string "yyyyy"
# ejemplo:
# 1 gatsu 4 nichi yyyyy