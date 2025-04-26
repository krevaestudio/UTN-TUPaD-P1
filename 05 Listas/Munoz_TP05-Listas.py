#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
nums_mult4 = []

for nm4 in range(1, 101):
    if nm4 % 4 == 0:
        nums_mult4.append(nm4)
print(nums_mult4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!
list_preferencias = ["Classical", "Roock", "Metal", "Pop", "Music Off"]
print(list_preferencias[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla.
list_lang = []
list_lang.append("Español")
list_lang.append("English")
list_lang.append("Deutsch")
print(list_lang)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla
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