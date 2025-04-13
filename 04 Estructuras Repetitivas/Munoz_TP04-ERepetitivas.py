#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for a in range(101):
    print(a)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
contador = 0
numerito = abs(int(input("Ingrese un número entero: ")))
if numerito == 0:
    print("El número tiene 1 dígito.")
else:
    while numerito > 0:
        numerito = numerito // 10
        contador += 1

print(f"El número tiene {contador} dígitos.")



#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
num_uno = int(input("Ingrese el primer número: "))
num_dos = int(input("Ingrese el segundo número: "))
sumatoria = 0
if num_uno > num_dos:
    num_uno, num_dos = num_dos, num_uno
    #Python permite intercambiar valores de variables con una sola linea sin usar auxiliares
    #Si num_uno es mayor a num_dos, las intercambiamos para usar una sola condicion
for x in range(num_uno+1, num_dos):
    sumatoria += x

print(f"La suma de todos los nums entre {num_uno} y {num_dos} es {sumatoria}.")



#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
suma=0
print("Ingrese números enteros para sumar (0 para salir):")
numerillo = int(input())

while numerillo != 0:
    suma += numerillo
    numerillo = int(input("Ingrese otro número (0 para salir): "))

print(f"La suma total de los numeros ingresados es {suma}")



#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
intentos = 1
misterioso = random.randint(0, 9)
print(f"<<< SOLO PARA TETSING >>> El numero es: {misterioso}")
print("Adivina el número | Pista: Está entre 0 y 9. Es entero")
adiv = int(input("El numero es... "))
while adiv != misterioso:
    intentos += 1
    adiv = int(input("No! El numero es... "))

print(f"Adininaste! El número era {misterioso}. Te tomó {intentos} intentos adivinarlo")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for f in range(100, -1, -2):
    print(f)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario
num_pos = int(input("Ingrese un número entero positivo: "))
suma = 0
if num_pos < 0:
    print("El número ingresado no es positivo. Lo convertiremos por usted")
    num_pos = abs(num_pos)
    print(f"Su numero ahora es {num_pos}")

for r in range(num_pos+1):
    suma += r

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
TOPE = 100 #Una "constante"
pares = 0
impares = 0
negativos = 0
positivos = 0

for nms in range(TOPE):
    num = int(input(f"Ingrese el número {nms+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print(f"De los {TOPE} números ingresados, {pares} son pares // {impares} son impares, {negativos} son negativos y {positivos} son positivos.")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
LIMITE = 100
suma = 0
for t in range(LIMITE):
    num = int(input(f"Ingrese el número {t+1}: "))
    suma += num

print(f"La media de los {LIMITE} números ingresados es {suma/LIMITE}.")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num_original = int(input("Ingrese un número entero: "))
num_invertido = 0
while num_original > 0:
    #sacamos el MOD del num original para obtener el ultimo digito
    digito = num_original % 10
    #multiplicamos el num para sumar un digito y le acoplamos el digito 
    num_invertido = num_invertido * 10 + digito
    #eliminamos el digito que ya usamos del numero original
    num_original //= 10

print(f"El número invertido es {num_invertido}")