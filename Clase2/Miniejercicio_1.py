#----------------------------------------------------------------------

#Miniejercicio 1: Dividir un número dado por 2 hasta que sea menor que 10e-4 y reportar número de divisiones

#----------------------------------------------------------------------

import sys

#Para trabajar desde la consola

#-------------------------

numero= float(sys.argv[1])

divisiones=0

#-------------------------

def division(n):

	return n/2

#-------------------------

while numero >= 10 ** -4:

	numero= division(numero)

	divisiones += 1

print (f"El número de divisiones es {divisiones}")

#-------------------------


