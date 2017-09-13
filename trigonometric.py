import numpy as np
import matplotlib.pyplot as plt
#Declaramos una funcion que nos devuelva f(x) = sin(pi*t+C) (C = El anio que ingrese a la universidad = 2015)
def f(t):
    return np.sin(np.pi*t+ 2015)
#Definimos el rango de dos variables y el intervalo en el que cambian
t1 = np.arange(0.0,2,0.001)
t2 = np.arange(0.0,2,0.125)
#Grafica la variable t1 contra la funcion f(t1) y grafica la variable t2 contra la funcion f(t)
plt.plot(t1, f(t1), 'g', t2, f(t2), 'r*')
#Le colocamos leyenda a la variable t
plt.xlabel('tiempo en la universidad (anios)')
#Guarda la grafica
plt.savefig('trigonometric.png')
#Muestra la grafica
plt.show()
