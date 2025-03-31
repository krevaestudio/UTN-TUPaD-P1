uno = 1
dos = 2
tres = 3
cuatro = 4
cinco = 5

print(f"es {uno} menor a {cuatro}?")
print(uno < cuatro)

print(f"es {uno} mayor o igual a 1?")
print(uno >= 1)

print(f"es 2 igual a {dos}?")
print(2 == dos)

print(f"es {tres} diferente a {dos}?")
print(tres != dos)

print(f"es {cinco} menor o igual a {dos}?")
print(cinco <= dos)

# Definición de constantes en Python
MAYOR_DE_EDAD = 18

edad_user = int(input("Ingrese su edad:"))
nombre_user = input("Ingrese su nombre:")
es_supervisor = input("Es supervisor? (si/no):")
es_empleado = input("Es empleado? (si/no):")

if edad_user >= MAYOR_DE_EDAD:
    if es_supervisor.lower() == "si":
        print(f"Hola {nombre_user}, al ser supervisor y constatar tu mayoria de edad podes acceder a todo el sistema")
    elif es_empleado.lower() == "si":
        print(f"Hola {nombre_user}, al ser empleado y constatar tu mayoria de edad podes acceder a tu sector.")
    else:
        print(f"Hola {nombre_user}, al ser mayor de edad pero no empleado podes consultar en administracion lo que necesites.")
else:
    print(f"Hola {nombre_user}, al ser menor de edad no podes acceder al sistema.")

if edad_user >= 75 and es_empleado:
    print(f"Al tener {edad_user} y trabajar (Es empleado? Rta: {es_empleado}) su contratacion esta fuera de la ley)")