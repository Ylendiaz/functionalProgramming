###################################### FUNCTIONAL PROGRAMMING#######################################

# FUNCION MAP

# La estructura de la función es: map(funcion a aplicar, objeto iterable)

#Obtener el cuadrado de todos los elementos en la lista.
def cuadrado(elemento=0):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = list( map(cuadrado, lista) )
#resultado = list( map( lambda elemento : elemento * elemento , lista) )
print(resultado)

# ----------------------------------------------------------------------------------

# FUNCION FILTER

# La estructura de la función es: filter(funcion a aplicar, objeto iterable)

#Obtener la cantidad de elementos mayores a 5 en la tupla.
def mayor_a_cinco(elemento):
    return elemento > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado = tuple(filter( mayor_a_cinco, tupla))
#resultado = tuple(filter( lambda elemento: elemento > 5, tupla))
print(resultado)

# ----------------------------------------------------------------------------------

# FUNCION REDUCE

# La estructura de la función es: reduce(funcion a aplicar, objeto iterable)

#Obtener la suma de todos los elementos en la lista
from functools import reduce

lista = [1,2,3,4]

def funcion_acumulador(acumulador=0, elemento=0):
    return acumulador + elemento

resultado = reduce(funcion_acumulador, lista)
#resultado = reduce(lambda acumulador=0, elemento=0: acumulador + elemento, lista)
print(resultado)

