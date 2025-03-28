#TP1 - Secuenciales
#Alumno: Andrés Muñoz
#Comision 25
import math

#1. Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#2. Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre “Hola Marcos!”
name = input("Decime tu nombre: ")
print(f"Hola, {name}!")

#3. Pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla "Soy N A, tengo X años y vivo en Y"
print("-------------------------------------------")
print("-------------------------------------------")
name = input("Ingrese su nombre: ")
last = input("Ingrese su apellido: ")
age = input("Escriba su edad: ")
home = input("Ingrese su ciudad de residencia: ")
print(f"Soy {name} {last}, tengo {age}, y vivo en {home}.")

#4. Pida el radio de un círculo e imprima por pantalla su área y su perímetro
radio = float(input("Establezca el radio de un círculo: "))
area = math.pi * radio**2
perim = 2*math.pi * radio
print(f"El area de un círculo con radio {radio} es {area}")
print(f"El perímetro de un círulo con radio {radio} es {perim}")

#5. Pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale
segs = int(input("Ingrese una cantidad de segundos: "))
print(f"{segs} equivale a {segs / 3600} hora(s)")

#6. Pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
num_mult = int(input("Ingrese un numero: "))
print(f"{num_mult} x 0 ={num_mult*0}")
print(f"{num_mult} x 1 = {num_mult*1}")
print(f"{num_mult} x 2 = {num_mult*2}")
print(f"{num_mult} x 3 = {num_mult*3}")
print(f"{num_mult} x 4 = {num_mult*4}")
print(f"{num_mult} x 5 = {num_mult*5}")
print(f"{num_mult} x 6 = {num_mult*6}")
print(f"{num_mult} x 7 = {num_mult*7}")
print(f"{num_mult} x 8 = {num_mult*8}")
print(f"{num_mult} x 9 = {num_mult*9}")
print(f"{num_mult} x 10 = {num_mult*10}")

#7. Pida al usuario dos números enteros distintos del 0 y muestre el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
num_one = int(input("Ingrese un numero (No ingrese 0): "))
num_two = int(input("Ingrese otro numero (No ingrese 0): "))
print("----------------------------------")
print(f"{num_one} + {num_two} = {num_one+num_two}")
print(f"{num_one} / {num_two} = {num_one/num_two}")
print(f"{num_one} x {num_two} = {num_one*num_two}")
print(f"{num_one} - {num_two} = {num_one-num_two}")

#8. Pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. (IMC = kg/(m**2))
peso_kg = float(input("Ingrese su peso (En kg): "))
altura_mts = float(input("Ingrese su altua (En Mts): "))
print(f"Su indice de masa corporal (IMC) es de {peso_kg/(altura_mts**2)}")


#9. Pida al usuario una temp en Celsius e imprima por pantalla su equivalente en Fahrenheit
g_cels = float(input("Ingrese una temperatura expresada en °C: "))
print(f"{g_cels}°C es equivalente a {g_cels+32}°F.")

#10. pida al usuario 3 números e imprima por pantalla el promedio de dichos números
num_one = int(input=("Ingrese un numero: "))
num_two = int(input=("Ingrese otro numero: "))
num_three = int(input=("Ingrese otro numero más: "))
promedio = (num_one+num_two+num_three)/3
print(f"El promedio de {num_one},{num_two} y {num_three} es {promedio}")