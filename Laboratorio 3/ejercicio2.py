a = [21, 8, 15, 3, 12]
b = [10, 9, 12, 15, 18]
c = [2, 3, 8, 9, 12]

concatenada = a + b + c
print(concatenada)

concatenada.insert(-1, 20)
print(concatenada)

concatenada.sort(reverse=True)
print(concatenada)

concatenada.append([4,5,6])
print(concatenada)

concatenada.remove([4,5,6])
print(concatenada)

concatenada.append(4)
print(concatenada)

concatenada.append(5)
print(concatenada)

concatenada.append(6)
print(concatenada)

suma_total = sum(concatenada)
print(suma_total)

promedio= sum(concatenada) / len(concatenada)
print(promedio)