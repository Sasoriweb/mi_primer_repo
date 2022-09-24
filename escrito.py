escritura1 = {"palabra" : "かさ", "significado" : "paraguas", "silabario" : "hiragana", "origen" : "Japón"}
escritura2 = {"palabra" : "ケーキ", "significado" : "torta", "silabario" : "katakana", "origen" : "Japón"}
escritura3 = {"palabra" : "本", "significado" : "libro","silabario" : "kanji", "origen" : "China"}
escritura4 = {"palabra" : "日", "significado" : "día" ,"silabario" : "kanji", "origen" : "China"}

lista_escrituras = [escritura1, escritura2, escritura3, escritura4]

def organizar_escritura(escritura):
    es_nivel_1 = escritura["silabario"] == "hiragana" 
    es_nivel_2 = escritura["silabario"] == "katakana"
    es_nivel_3 = escritura["silabario"] == "kanji"
    palabra = escritura["palabra"]
    significado = escritura["significado"]
    origen = escritura["origen"]
    silabario = escritura["silabario"]
    if es_nivel_1 and not es_nivel_2:
        return f"La palabra {palabra} significa {significado}, pertenece al silabario {silabario} y es de origen {origen}"
    elif es_nivel_2:
        return f"{escritura} Nivel básico B"
    else:
        return f"{escritura} Nivel Avanzado"

for escritura in lista_escrituras:
    print(organizar_escritura(escritura))

