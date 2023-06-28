pacientes = []  

for i in range(3):
    nombre = input("Ingrese el nombre del paciente: ")
    peso = float(input("Ingrese el peso del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente: "))

    while True:
        try:
            edad = int(input("Ingrese la edad del paciente: "))
            if edad > 0: 
                break
            else:
                print("La edad debe ser mayor que cero.")
        except ValueError:
            print("Error: La edad debe ser un número entero.")

    paciente = (nombre, peso, estatura, edad)  
    pacientes.append(paciente)  

print("Información de los pacientes: \n")
for paciente in pacientes:
    print("Nombre:", paciente[0])
    print("Peso:", paciente[1])
    print("Estatura:", paciente[2])
    print("Edad:", paciente[3])
    print()
