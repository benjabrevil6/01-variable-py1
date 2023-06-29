Temperaturas_Mínimas = {9, 5, 2, 7, 6, 1}
Temperaturas_Máximas = {12, 14, 11, 10, 15, 9}

if 9 in Temperaturas_Mínimas and 9 in Temperaturas_Máximas:
    print("La temperatura 9° si se encuentra en los 2 grupos.")
else:
    print("La temperatura 9° no se encuentra en los 2 grupos.")

if 6 in Temperaturas_Mínimas and 17 in Temperaturas_Máximas:
    print("Las temperaturas 6° y 17° si se encuentran en algunos de los grupos. ")
else:
    print("Las temperaturas 6° y 17° no se encuentran en algunos de los grupos. ")

min_4= [tem ** 4 for tem in Temperaturas_Mínimas] 
max_4= [tem ** 4 for tem in Temperaturas_Máximas]

print("Las temperaturas minimas aumentadas 4 veces son:",min_4)
print("Las temperatuas máximas aumentadas 4 veces son:",max_4)

grupo= min_4+max_4
print(grupo)