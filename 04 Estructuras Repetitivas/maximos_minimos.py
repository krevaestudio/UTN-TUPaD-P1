#En Python podemos usar la cadena -inf convertida a float para representar el menor número posible
# y la cadena inf convertida a float para representar el mayor número posible.

num_max = float('-inf')
tope = 5

for contador in range (tope):
    print(f"Ingrese un numero ({contador+1}/{tope}):")
    num = int(input())
    if num > num_max:
        num_max = num

print(f"El número máximo es: {num_max}")