#----------------------------------------------------------------------------------

#Calculadora de promedio de números dados

#----------------------------------------------------------------------------------

import statistics

from sys import argv

def calcuprom(lista):

	"""

	Función que calcula el promedio de números dados

	Input: list (Lista de números para los cuales se calcularáel promedio)

	Output: float (promedio calculado a partir de los números)

	"""

	return statistics.mean(lista)


archivo= argv[1]

numeros= []

with open(archivo) as f:

	for linea in f:
		numeros.append(float(linea.strip()))

promedio= calcuprom(numeros)

print(promedio)
