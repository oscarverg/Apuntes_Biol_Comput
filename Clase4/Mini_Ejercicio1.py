#------------------------------------------------------------------------------------------

#Mini Ejercicio 1: Genere una sucesión de 0s y 1s que representan lanzamientos de monedas. Calcule indicadores
#estadísticos de sus datos usando statistics y pandas

#------------------------------------------------------------------------------------------

import random
import statistics as st
import pandas as pd

#------------------------------

#Cálculo de estadígrafos a partir de Statistics

sucesion= [random.randint(0,1) for i in range(1000)]

mediast= st.mean(sucesion)
print (f"La media de los lanzamientos a partir de statistics es {mediast}")

medianst= st.median(sucesion)
print (f"La mediana de los lanzamientos a partir de statistics es {medianst}")

modest= st.mode(sucesion)
print (f"La moda de los lazamientos a partir de statistics es {modest}")

variancest= st.variance(sucesion)
print (f"La varianza de los lanzamientos a partir de statistics es {variancest}")

desvst= st.stdev(sucesion)
print (f"La desviación estándar de los lanzamientos a partir de statistics es {desvst}")

#--------------------------------

#Cálculo de estadígrafos a partir de pandas

print ("")
print ("Indicadores estadísticos de Pandas")
print ("")
df= pd.DataFrame(sucesion)

descriptivospanda= df.describe()

print (descriptivospanda)


