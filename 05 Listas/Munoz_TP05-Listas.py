#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
nums_mult4 = []

for nm4 in range(1, 101):
    if nm4 % 4 == 0:
        nums_mult4.append(nm4)
print(nums_mult4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo
list_preferencias = ["Classical", "Roock", "Metal", "Pop", "Music Off"]
print(list_preferencias[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante 
list_lang = []
list_lang.append("Español")
list_lang.append("English")
list_lang.append("Deutsch")
print(list_lang)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#para testear:
numeros.remove(max(numeros))
print(numeros)
print("Viendo lo anterior, lo que hace el programa es ir eliminando el número de mayor valor de la lista")
print("En el codigo original, se elimina el 22; y en el que repeti para testear, se elimina el 15. Comprobando lo mencionado arriba")

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar los 2 primeros
numeros = []
for i in range(10, 31, 5):
    numeros.append(i)
print(numeros[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1:3] = ["Sandero", "Idea Adventure"]

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante
dobles = []
for i in [5, 10, 15]:
    dobles.append(i * 2)
print(dobles)

#9) Dada la siguiente lista, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan","leche"],["arroz","fideos","salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
#d) Imprimir la lista resultante por pantalla
print(f"todas las compras: {compras}")
print(f"compras del primer cliente: {compras[0]}")
print(f"compras del segundo cliente: {compras[1]}")
print(f"compras del tercer cliente: {compras[2]}")

#10) Crear una lista anidable llamada "lista_anidada" que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)