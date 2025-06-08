#Definicion de funciones
def entero_valido(msje, min = float("-inf"), max = float("inf")):
    #La funcion espera 3 paramentros. Pero si min o max no llegan, min va a ser por default -infinito
    #y max va a ser infinito. Si llega una, esa una se transforma en el paramentro
    nm = int(input(f"{msje}"))
    while nm < min or nm > max:
        nm = int(input(f"Error! {msje}"))
    return nm

def obtener_resto(n1,n2):
    return n1 - n2 * (n1//n2)
def es_multiplo(f,g):
    #Esto va a comparar el resutado con el cero y devuelve True o False
    return obtener_resto(f,g) == 0

def es_perfecto(nx):
    return sum_divisores_propios(nx) == nx

def sum_divisores_propios(a):
    sumatoria = 0
    for i in range(1, (a//2)+1):
        if es_multiplo(a,i):
            sumatoria+=i
    return sumatoria



def informar_perfekt(x):
    if es_perfecto(x):
        print(f"El numero {x} es perfecto")
    else:
        print(f"El numero {x} NO es perfecto")



#Main
num = entero_valido("Ingrese un numero natural:",1)
informar_perfekt(num)