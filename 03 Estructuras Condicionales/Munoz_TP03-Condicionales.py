# NOTA DEL ALUMNO: varios ejercicios pueden estar relacionados
# por lo que los resolveré juntos de ser posible o usare las variables de los anteriores
# Ejemplo: ejercicio 1 pide una edad para evaluar y el 4 tambien 

from statistics import mode, median, mean #Para ejercicio 6
import random #Para ejercicio 6

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

#5. permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por
#pantalla "Ha ingresado una contraseña correcta"; en caso contrario, imprimir
#"Por favor, ingrese una contraseña de entre 8 y 14 carac"

pswrd = input("Ingrese una contraseña de entre 8 y 14 caracteres:")

if len(pswrd) >= 8 and len(pswrd) <= 14:
    print(f"Ha ingresado una contraseña correcta. Su contraseña tiene {len(pswrd)} caracteres")
else:
    print(f"Por favor, ingrese una contraseña de entre 8 y 14 caracteres! Su contraseña tiene {len(pswrd)} caracteres")

#6. Usando Statistics. Escribir un programa que  la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare p determinar si
#hay sesgo positivo, negativo o no hay. Imprimir el resultado

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
#SESGO POSITIVO: Cuando la media es mayor que la mediana y la mediana es mayor que la moda
#SESGO NEGATIVO: Cuando la media es menor que la mediana y la mediana es menor que la moda
#SIN SESGO: Cuando la media es igual a la mediana y la mediana es igual a la moda

print(f"Lista de numeros aleatorios: {numeros_aleatorios}")
print(f"Moda: {mode(numeros_aleatorios)}")
print(f"Mediana: {median(numeros_aleatorios)}")
print(f"Media: {mean(numeros_aleatorios)}")

if mode(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mean(numeros_aleatorios):
    print("Hay sesgo positivo")
elif mode(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mean(numeros_aleatorios):
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")

#7. solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
#añadir un signo de exclamación al final e imprimir el string resultante
#en caso contrario, dejar el string tal cual lo ingresó el usuario
frase = input("Ingrese una frase: ")
#toma el ultimo index y leresta 1 para obtener el ultimo caracter
if frase[-1].lower() in "aeiou":
    #Lo compara con aeiou en minuscula siempre, caracter por caracter de "aeiou"
    print(f"{frase}!")
else:
    print(frase)


#Otros ejemplo solo para testear
ej1 = "Hola"
ej2 = "Adios"
ej3 = "Python"
ej4 = "Banana"
if ej1[-1].lower() in "aeiou":
    print(f"{ej1}!")
else:
    print(ej1)

if ej2[-1].lower() in "aeiou":
    print(f"{ej2}!")
else:
    print(ej2)

if ej3[-1].lower() in "aeiou":
    print(f"{ej3}!")
else:
    print(ej3)

if ej4[-1].lower() in "aeiou":
    print(f"{ej4}!")
else:
    print(ej4)

#8. solicite al usuario su nombre y que ingrese 1, 2, 3 dependiendo:
#1 Si quiere su nombre en mayúsculas
#2 Si quiere su nombre en minúsculas
#3 Si quiere su nombre con la primera letra mayúscula

name = input("Ingrese su nombre: ")
print(f"""Hola {name}, por favor ingresa una de estas opciones (Solo el numero
    1. Escribir mi nombre en mayusculas
    2. Escribir mi nombre en minusculas
    3. Escribir mi nombre con la primera letra mayuscula""")
opcion = int(input("Ingrese una de las opciones: "))
if opcion == 1:
    print(name.upper())
elif opcion == 2:
    print(name.lower())
elif opcion == 3:
    print(name.title())
else:
    print("Opcion no valida. Vuelva a intentarlo")

#9. Pida al user la magnitud de un terrem, clasifique en categorias segun richter
#Menor que 3 = Muy Leve (Imperceptible)
#Mayor o igual que 3 y menor que 4 = Leve (Ligeramente perceptible)
#Mayor o igual que 4 y menor que 5 = Moderado (Sentido x personas. Gralmente no causa daños)
#Mayor o igual que 5 y menor que 6 = Fuerte (Puede causar daños en estruc debiles)
#Mayor o igual que 6 y menor que 7 = Muy Fuerte (Puede causar daños signific)
#Mayor o igual que 7 = Extremo (Puede causar daños graves a gran escala)
prefrase= "En base a lo ingresado, el terremoto es "
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud >= 7:
    print(f"{prefrase}Extremo - Puede causar daños graves a gran escala")
elif magnitud >= 6 and magnitud < 7:
    print(f"{prefrase}Muy Fuerte - Puede causar daños significativos")
elif magnitud >= 5 and magnitud < 6:
    print(f"{prefrase}Fuerte - Puede causar daños en estructuras debiles")
elif magnitud >= 4 and magnitud < 5:
    print(f"{prefrase}Moderado - Sentido por personas, pero generalmente no causa daños")
elif magnitud >= 3 and magnitud < 4:
    print(f"{prefrase}Leve - Ligeramente perceptible")
else:
    print(f"{prefrase}Muy Leve - Imperceptible")

#10. Utilizando info de la tabla aportada (Incluida como captura de pantalla en esta carpeta)
# Preguntar al user en que hemisgerio esta
# que mes del año es y que dia. Devolver si es verano, otoño, invierno o primavera
hemis = input("Ingrese el hemisferio en el que se encuentra (N/S): ")
mes = int(input("Ingrese el mes corriente(1-12): "))
dia = int(input("Ingrese el dia (1-31): "))

if hemis.upper() == "N":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Es Invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Es Primavera")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Es Verano")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes ==12 and dia <=20):
        print("Es Otoño")
    else:
        print("Fecha no valida. Vuelva a intentarlo")
elif hemis.upper() == "S":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Es Verano")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Es Otoño")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Es Invierno")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes ==12 and dia <=20):
        print("Es Primavera")
    else:
        print("Fecha no valida. Vuelva a intentarlo")
else:
    print("Hemisferio no valido. Vuelva a intentarlo")