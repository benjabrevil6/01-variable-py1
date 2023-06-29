#EJERCICIO 1#

trabajadores = [
    ['Juan',[700000,650000,690000]], 
    ['María',[681000,710000,590000]], 
    ['Pedro',[590000,635000,705000]]
    ]

def prome_su(trabajadores):
    promedio_juan  = sum(trabajadores[0][1]) / len(trabajadores[0][1])
    promedio_maria = sum(trabajadores[1][1]) /len(trabajadores[1][1])
    promedio_pedro = sum(trabajadores[2][1]) / len(trabajadores[2][1])
    
    print('El promedio de Juan es:',round(promedio_juan,2))
    print('El promedio de María es:',round(promedio_maria,2))
    print('El promedio de Pedro es:',round(promedio_pedro,2))

def sueldo(trabajadores):
    sueldo_juan  = max(trabajadores[0][1])
    sueldo_maria = max(trabajadores[1][1])
    sueldo_pedro = max(trabajadores[2][1])
    
    print('El sueldo más alto de Juan es:', sueldo_juan)
    print('El sueldo más alto de Maria es:', sueldo_maria)
    print('El sueldo más alto de Pedro es:', sueldo_pedro)



def rete_impu(trabajadores):
    total_juan  = sum(trabajadores[0][1])
    total_maria = sum(trabajadores[1][1])
    total_pedro = sum(trabajadores[2][1])
    
    impuesto_juan  = total_juan * 0.1225
    impuesto_maria = total_maria * 0.1225
    impuesto_pedro = total_pedro * 0.1225
    
    retencion_impuestos = (impuesto_juan, impuesto_maria, impuesto_pedro)
    mayor_impuesto = max(retencion_impuestos)
    
    print('La retención de impuestos de Juan es de:',impuesto_juan)
    print('La retención de impuestos de Maria es de:',impuesto_maria)   
    print('La retención de impuestos de Pedro es de:',impuesto_pedro) 
    print('El mayor impuesto retenido es de:',mayor_impuesto) 

print("#####")
prome_su(trabajadores)
print("#####")
sueldo(trabajadores)
print("#####")
rete_impu(trabajadores)
