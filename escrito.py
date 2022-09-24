escritura1 = {"palabra" : "かさ", "significado" : "paraguas", "silabario" : "hiragana", "origen" : "Japón"}
escritura2 = {"palabra" : "ケーキ", "significado" : "torta", "silabario" : "katakana", "origen" : "Japón"}
escritura3 = {"palabra" : "本", "significado" : "libro","silabario" : "kanji", "origen" : "China"}


def organizar_escritura(escritura):
    es_nivel_1 = escritura["silabario"] == "hiragana" 
    es_nivel_2 = escritura["silabario"] == "katakana"
    es_nivel_3 = escritura["silabario"] == "kanji"
    palabra = escritura["palabra"]
    if es_nivel_1 and not es_nivel_2:
        return f"{escritura1} Nivel básico A"
    elif es_nivel_2:
        return f"{escritura2} Nivel básico B"
    else:
        return f"{escritura3} Nivel Avanzado"

print(organizar_escritura(escritura1))
print(organizar_escritura(escritura2))
print(organizar_escritura(escritura3))


