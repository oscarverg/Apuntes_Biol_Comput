#--------------------------------------------------------

#Mini ejercicio 3: Repetir el ejercicio anterior pero sacando solo los numeros primos

#--------------------------------------------------------

lista= list(range(1, 1001))

noprimos= []

for e in lista:

	if e < 2:
		primos = False

	#Cualquier numero menor a 2 no es primo (es decir, 1 no es primo)

	else:

		primos= True

		#Esto hace que siempre se partira asumiendo que el numero es primo, hasta que se demuestre lo
		#contrario

		for i in range(2, e):

		#Por cada elemento en el rango de 2 al número evaluado hace una division
			if e % i == 0:

		#Y si esa division tiene resto 0, significa que no es primo

				primos= False
				break

	if primos == False:

		noprimos.append(e)

print (noprimos)
