


# bonus:
# si los dias en japones ocupan una y en su nombre real (yokka)
# concatenar el string "yyyyy"
# ejemplo:
# 1 gatsu 4 nichi yyyyy
dias = range(1,32) # esto va a ser un listado de integers (del 1 al 31)
meses = range(1,13) #esto va a ser un listado de integers (del 1 al 12)


# implementar un listado de fechas en japonés
# utilizando dias y meses
kanji_gatsu = " 月 "
kanji_nichi = " 日 "
for mes in meses:
    for dia in dias:
        if dia in [4,8,14,24] :
            print(str(mes) + kanji_gatsu + str(dia) + kanji_nichi + "yyyy")
        else:
            print(str(mes) + kanji_gatsu + str(dia) + kanji_nichi)
     