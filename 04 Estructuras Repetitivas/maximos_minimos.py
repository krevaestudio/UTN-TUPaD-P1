#En Python podemos usar la cadena -inf convertida a float para representar el menor número posible
# y la cadena inf convertida a float para representar el mayor número posible.

num_max = float('-inf')
num_min = float('inf')
tope = 5

for contador in range (tope):
    print(f"Ingrese un numero ({contador+1}/{tope}):")
    num = int(input())
    if num > num_max:
        num_max = num
    elif num < num_min:
        num_min = num

print(f"El número máximo es: {num_max}. El número mínimo es: {num_min}.")


#Para hacer codigo de forma eficiente y no hacer dos IFs para las posiciones, conviene
#establecer el primer número como el máximo y el mínimo, y luego comparar los demás números con esos valores.
# Esto se hace, metiendoe l ptimer número en la variable num_max y num_min fuera del bucle.
tope = 8

print(f"Ingrese un numero (1/{tope}):")
num1 = int(input())
numero_max = num1
numero_min = num1
pos_min = 1
pos_max = 1

for ctdr in range (2,tope+1):
    print(f"Ingrese un numero ({ctdr}/{tope}):")
    num1 = int(input())
    if num1 > numero_max:
        numero_max = num1
        pos_max = ctdr
    elif num1 < numero_min:
        numero_min = num1
        pos_min = ctdr

print(f"El número máximo es: {numero_max} y esta en la posicion {pos_max}. El número mínimo es: {numero_min} y esta en la posicion {pos_min}.")