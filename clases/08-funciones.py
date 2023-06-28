#01-DECLARANDO LA PRIMERA FUNCIÓN
print("################## 01-DECLARANDO UNA FUNCIÓN SIMPLE ##################")

def mi_primera_funcion():
    print("Esta es mi primera función")


mi_primera_funcion()

#02-DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS
print("\n################## 02-DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS ##################")

def concatenar(lista1,lista2):
    return lista1 + lista2;

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar()
print(concatenar(lista1,lista2));

#03-DECLARANDO UNA FUNCIÓN MULTIPLICACION PASANDO PARAMETROS
print("\n################## 03-DECLARANDO UNA FUNCIÓN MULTIPLICACION PASANDO PARAMETROS ##################")

def multiplicacion (num1,num2):
    return num1*num2

#multiplicacion()
print(multiplicacion(5,5))


#04-EJEMPLO DE UNA FUNCIÓN
print("\n################## 04-FUNCIONES SUMA Y RESTA (POR TECLADO) ##################")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

#Se llama a la función Suma
resultado = suma(a, b)
print("La suma es de:", resultado)

#Se llama a la función resta
resultado2 = resta(a, b)
print("La resta es de:", resultado2)