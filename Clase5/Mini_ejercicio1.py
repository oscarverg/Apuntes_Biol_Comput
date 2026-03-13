#-----------------------------------------------------

#Mini ejercicio 1: Crear una clase Cuadrado que reciba como entrada el largo de sus aristas. Cree una
#función de clase que entregue el área del cuadrado.

#-----------------------------------------------------


class Cuadrado():

	"""
	Clase que representa un Cuadrado.

	Atributos:

	lado: float (Largo de los lados del cuadrado)

	"""
	def __init__ (self, lado):

		"""

		Función iniciadora de la clase

		"""

		self.lado= lado

	def area(self):

		"""

		Función que devuelve el area del cuadrado.

		"""

		return self.lado **2

elado= Cuadrado(4)

elarea= elado.area()

print (elarea)
