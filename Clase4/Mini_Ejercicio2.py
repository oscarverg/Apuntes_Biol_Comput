#----------------------------------------------------------------------------

#Mini Ejercicio 2: Considere la función f(x) = sin x , y encuentre numéricamente un mínimo con scipy.minimize. Qué
#pasa con los otros mínimos?

#-----------------------------------------------------------------------------
import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

#----------------------------


def f(x): return np.sin(x)

domx= np.linspace (-4, 4,1000)

domy= [f(x) for x in domx]

sol= minimize_scalar (f)

plt.scatter(sol.x, f(sol.x))

plt.plot(domx, domy); plt.show()
