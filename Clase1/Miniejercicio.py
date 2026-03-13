#--------------------------------------------------

import sys

#librería para poder mandar argumento desde la consola

#-------------------------------------------------


def espar(n):

	if n % 2 == 0:
		print ("Es par")

	else:
		print ("No es par")


numero= int(sys.argv[1])
espar(numero)
