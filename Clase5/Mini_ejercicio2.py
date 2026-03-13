#-----------------------------------------------------------------------------

#Mini ejercicio 2: Cree una clase Cubo que reciba como entrada el largo de sus aristas.
#Cree una función de clase que entregue el área del cubo

#-------------------------------------------------------------------------------

class Cubo:

	"""
	Clase que representa un Cubo

	Atributos:

	lado: float (Largo de los lados del cubo)

	"""

	def __init__ (self,lado):

		"""
		Función iniciadora de la clase

		"""

		self.lado= lado

	def area (self):

		"""

		Función que devuelve el área del cubo a partir del largo de los lados

		"""

		return self.lado **3


elado= Cubo(4)

elarea= elado.area()

print (elarea)
