for x in range (5):
    print(x, "hola")
    #imprime 0 1 2 3 4

for y in range(2,5):
    print(y, "adios")
    #imprime 2 3 4 5 6 7

for z in range(8,2,-2):
    print(z, "perro")

w = 5

while w > 0:
    print (f"Contemos hasta el kaboom: {w}")
    w -= 1


#Contraseña de 10 caracteres | Ejemplo de corte con centinela o bandera
contra = ""
while len(contra) < 10:
    contra = input("Ingrese una contraseña (MAYOR A 10 CARACTERES): ")
    if len(contra) < 10:
        print("ERROR")

print("Contraseña aceptada")


#EJEMPLO DE WHILE CON CONTADOR + BANDERA

sueldo_anual = 0
cont_meses = 1

print("""-------------------------------------------------------------------")
    MEGA FACTURACION SYSTEM - UN SISTEMA DE CONTROL DE SUELDOS
    by Nerea | Para finalizar ingrese 0 o valor negativo
    -------------------------------------------------------------------""")

print("Ingrese el sueldo cobrado en el mes",cont_meses)
sueldo_mensual = float(input())
while cont_meses < 12 and sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual
    cont_meses += 1
    print("Ingrese el sueldo cobrado en el mes",cont_meses)
    sueldo_mensual = float(input())
if sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual

print("El sueldo anual es de: $", sueldo_anual)