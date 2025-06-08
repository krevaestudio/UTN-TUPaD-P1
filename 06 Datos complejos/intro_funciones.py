nombre = input ("Escribi tu nombre: ")

print(f"Tu nombre ({nombre}) tiene {len(nombre)} caracteres")
# LEN es una funcion que ya viene definida en Python


#DEFinicion de funciones
def obtener_resto(n1,n2):
    return n1 - n2 * (n1//n2)
def es_multiplo(f,g):
    #Esto va a comparar el resutado con el cero y devuelve True o False
    return obtener_resto(f,g) == 0

def eldoble(nx):
    return nx*2

def next_num(num):
    return num+1


#PROGRAMA PRINCIPAL
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
resto = obtener_resto(a,b)

print(f"El resto entre {a} y {b} es {resto}")
print(f"Es multiplo? {es_multiplo(a,b)}")

print("El doble del siguiente de ",a," es:")
print(eldoble(next_num(a)))
