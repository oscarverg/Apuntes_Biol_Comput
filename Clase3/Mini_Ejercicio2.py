#--------------------------------------------------------------------------

#Mini ejercicio 2: Cree un programa que sume todos los números dados al programa:

#Ej:  $python programma.py 2 3 4 5
#     Los números suman 14

#---------------------------------------------------------------------------

from sys import argv

lista_sum= argv[1:]

numeros= [int(i) for i in lista_sum]

#convierte cada elemento de la lista (originalmente strings por el argv) a enteros

coso= sum(numeros)

print (f"Los números suman {coso}")


#--------------------------------------------------------------------------
