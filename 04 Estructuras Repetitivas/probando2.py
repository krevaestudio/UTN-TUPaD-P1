#Programa que imprima los pares entre un numero ingresado por el user y 0
#debe imprimirlos en una sola linea, separados por espacio

numero = int(input("Ingrese un numero: "))
if numero > 0:
    if numero % 2 != 0:
        numero = numero - 1
    cont = numero
    while cont >= 0:
        print(cont, end=" ")
        cont = cont - 2
else:
    print("El numero ingresado no es positivo. Error del programa!")


#Ejemplo de corte de programa con while y un valor de corte
CORTE = '*'
edad_minima = float("inf")
NOMB_INVALIDO = "NO-DEFINIDO"
nombre_minima = NOMB_INVALIDO

nombre = input(f"Ingrese un nombre (o ingrese {CORTE} para salir): ")
while nombre != CORTE:
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    #Proceso 
    if edad < edad_minima:
        edad_minima = edad
        nombre_minima = nombre
    nombre = input(f"Ingrese otro nombre nombre (o ingrese {CORTE} para salir): ")

if nombre_minima == NOMB_INVALIDO:
    print("No se ingresaron personas.")
else:
    print(f"La persona más chica es {nombre_minima} y tiene {edad_minima} años.")