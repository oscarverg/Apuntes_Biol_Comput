#---------------------------------------------------------------------------------------------

#MMini ejercicio 3: Cree un programa que pida su edad y sexo con input, y con eso le diga los años
#que le quedan para jubilar. Si laedad no es un entero positivo, le debe volver a pedir la edad
#hasta que lo sea

#--------------------------------------------------------------------------------------------

#EDAD DE JUBILACIÓN DE LOS CHILENOS Y CHILENAS!!!


#Chilenos: 65 años

#Chilenas: 60 años

#--------------------------------------------------------------------------------------------

sexo= input("Bienvenido/a.Ingresa tu sexo (hombre/mujer):")

while True:

	edad= input("Ahora ingresa tu edad:")

	if edad.isdigit() and int(edad)>0:

		edad= int(edad)
		break

	else:
		print ("Porfavor ingresar una edad valida (entero positivo)")


if sexo.lower()== "mujer" or sexo.lower() == "femenino":

	años_rest= 60 - edad

	if años_rest >= 60:

		print (f"Muchas gracias. Ya puedes recibir pensión")

	else:
		print (f"Muchas gracias. Te quedan {años_rest} añospara jubilar")

elif sexo.lower()== "hombre" or sexo.lower()== "masculino":

	años_rest= 65 - edad

	if años_rest >= 65:

		print (f"Muchas gracias. Ya puedes recibir pensión")

	else:

		print (f"Muchas gracias. Te quedan {años_rest} años para jubilar")

else:

	print (f"Error en el sistema")
