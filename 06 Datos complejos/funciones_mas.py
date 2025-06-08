#EJEMPLO DE PROGRAMA MODULARIZADO
#Detectar si un numero es primo



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

def es_primo(z):
    cont = 2
    #Mientras el contador sea menor al numero
    #y el numero no sea multiplo de contador
    while cont < z and not es_multiplo(z,cont):
        #sigue chequeando
        cont +=1
        #retrona si el contador es igual al numero (T= es primo, F= no es primo)
    return cont == z 

def informar_es_primo(x):
    if es_primo(x):
        print(f"El numero {x} es primo")
    else:
        print(f"El numero {x} NO es primo")




#Main
num = entero_valido("Ingrese un numero natural:",1)
#Enviamos el mensaje como arg, y el valor de min como arg; por lo tanto el min sera 1 y el max +infinito
informar_es_primo(num)