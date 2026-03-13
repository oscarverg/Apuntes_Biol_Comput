#------------------------------------------------------------------

#Mini ejercicio 2: Crear una lista con números hasta 1000 y luego quitar todos los impares

#---------------------------------------------------------------

lista= list(range(1,1001))

sinimpares= []

for e in lista:
	if e % 2 == 0:
		sinimpares.append(e)

print (sinimpares)
