def contar_palabras(oracion):
    palabras = oracion.split()
    resultado={}

    for palabra in palabras:
        longitud = len(palabra)
        resultado[palabra] = longitud

    return resultado

oracion= input("Ingrese una oración: ")
dic= contar_palabras(oracion)
print(dic)