#Listas en Python
#Las listas son estructuras de datos que permiten almacenar múltiples elementos en una sola variable
#Las listas pueden contener elementos de diferentes tipos, incluyendo otras listas
#Las listas son mutables

list_num = [1, 2, 3, 4, 5, 6]
list_wrd = ["Ains", "Zwei", "Drei", "Vier", "Funf", "Sechs"]
list_ran = ["Uno", "Dos", 3, 4, True, "Mandanga",1.7]
frase = "Das ist eine Liste"
print(list_wrd)
list_wrd.append("Sieben") # Agregar un elemento al final de la lista
print(list_wrd)

list_num.remove(4) # Eliminar un elemento de la lista
print(list_num)

list_numwrd = list_num + list_wrd # Concatenar listas
print(list_numwrd)

#comprobar si un elemento está en la lista
print("Zwei está en la lista list_wrd?")
print('Zwei' in list_wrd) # True

print("Ocho esta en la lista list_wrd?")
print('Ocho' in list_wrd) # False

german_wrds = frase.split() # Dividir una cadena en una lista de palabras
print(german_wrds)

#Listas anidadas
rammstein = ["Liebe ist für alle da", ["Radio", "Deutschland","Adieu"], "Mutter", "Herzeleid", "Rosenrot", ["Amerika", "Hallelujah"], "Volkerball"]
print(rammstein[1])
print(rammstein[1][0]) # Acceder Radio