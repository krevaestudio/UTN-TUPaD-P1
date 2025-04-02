# NOTA DEL ALUMNO: varios ejercicios pueden estar relacionados
# por lo que los resolveré juntos de ser posible o usare las variables de los anteriores
# Ejemplo: ejercicio 1 pide una edad para evaluar y el 4 tambien 


#1. Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
#4. Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

if edad < 12:
    #Niño/a: menor de 12 años.
    print("Es un niño")
elif edad >= 12 and edad < 18:
    #Adolescente: mayor o igual que 12 años y menor que 18 años.
    print("Es un adolescente")
elif edad >= 18 and edad < 30:
    #Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    print("Es un adulto joven")
else:
    #Adulto/a: mayor o igual que 30 años.
    print("Es un adulto")

#2.solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota= int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3. permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par
numero= int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print(f"Ha ingresado un numero par. {numero} es par")
else:
    print(f"Por favor, ingrese un numero par. {numero} NO es par")