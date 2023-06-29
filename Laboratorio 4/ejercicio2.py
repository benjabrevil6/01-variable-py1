##EJERCICIO 2##

a = [10,80,15,30,20]
b = [20,45,80,20,10]
c = [20,35,60,90,20]

print("#ITEM A")

def common_value(a, b, c):
    val = list(set(a) & set(b) & set(c))
    return val

print("#ITEM B")

def sum_list(a, b, c):
    lista = a + b + c
    return lista

print("#ITEM C")

def nothing_repeat(lista):
    repeat_list = list(set(lista))
    return repeat_list

print("#ITEM D")

def order_list(no_duply):
    order_lista = sorted(no_duply, reverse=True)
    return order_lista

print("ITEM E")

def num_replace(order_lista):
    copy_list = order_lista.copy()
    copy_list[6] = 100
    return copy_list

val = common_value(a, b, c)
lista = sum_list(a, b, c)
no_duply = nothing_repeat(lista)
order_lista = order_list(no_duply)
final_list = num_replace(order_lista)

print(f'Valores en comun de las 3 listas: {val}')
print(f'Concatenación de las 3 listas: {lista}')
print(f'Eliminación de duplicados: {no_duply}')
print(f'Ordenando la lista de forma descendente: {order_lista}')
print(f'Reemplazando la posicion 7° por un 100: {final_list}')


