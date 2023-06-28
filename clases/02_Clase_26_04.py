#LISTA: Todo tipo de valores
#TUPLA: No mutables
##INSTALAR: "Live Share" "Material Icon Theme" "Bookmarks" "Pylance" "Error Lens" "Guides"

K = 60.5
##print("tú pesas {M} kilos") MALO falta una f
print(f"tú pesas {K} kilos")
print("tú pesas", int(K) ,"kilos")

Peso = 120
Altura = 1.8
IMC = Peso/(Altura)**2
print(IMC)
#ACORTAR DECIMALES

print("Tu IMC es de: {:.2f}".format(IMC))

#Podemos transferir cualquier valor a un Booleano
print(bool(0)) #Python detecta 0 como falso
print(bool("")) #Python detecta un vacio como falso
print(bool(None)) #Python detecta La Nada como falso
print(bool("False")) #Python detecta un "Texto" como verdadero
print(bool(1)) #Python detecta 1 como verdadero
print(bool("\n")) #Python detecta un "Texto" como verdadero

#Inicializando listas de 2 maneras
L = [0,1,2,3,4]
lista_números = list([0,1,2,3])

print(lista_números)
print(L)

#LISTA DE DATOS COMPUESTOS 
data=["Osorno", {"UV":"nivel bajo"}]
print(data[1])


#OTRA LISTA DE DATOS MIXTOS
data_asig=[10023, "Programación",1 ,True]
cod,ramo,semeste,estado=data_asig
print(ramo)

#LISTA EXPRESS
print(list("Python"))
print(list(range(20)))
print("\n")

##TUPLAS
#count (contar datos en tupla)
#index (posición en tupla)

#INICIAR SET
conjunto_vacio=set()
print(type(conjunto_vacio))
conjunto_vacio.add("El Pepe")
print(conjunto_vacio)


#DICCIONARIO 
#como las listas, god
diccionario = dict()
diccionario={}

datos_personales = {
    "Nombre":"Victor",
    "Institución":"Ulagos",
    "Edad":29,
    "Asignaturas":{"Estructura de Datos","Programación"}
}
print(datos_personales)
print(datos_personales["Institución"])
datos_personales["Institución"] = "USS"
print("Diccionario actualizado", datos_personales)

#AÑADIR DATOS
datos_personales["Ciudad"] = "Osorno"
print("Diccionario con el nuevo campo", datos_personales)

#BORRAR DATOS
del datos_personales["Ciudad"]
print("Sin Osorno", datos_personales)
