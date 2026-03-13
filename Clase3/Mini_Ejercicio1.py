#--------------------------------------------------------------------

#Mini ejercicio 1: Cree un script que lea un archivo que tenga un número por fila y los sume

#-------------------------------------------------------------------

from sys import argv

e= 0



with open("ejemplo.txt", "r") as f:

	for i in f:

		e += int(i)

print (e)

#------------------------------------------------------------------
