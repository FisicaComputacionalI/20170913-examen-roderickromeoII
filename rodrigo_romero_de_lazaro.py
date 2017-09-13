import numpy as np
import matplotlib.pyplot as plt
#Declaramos una funcion que nos devuelva f(x) = exp(-x)* cos (2pi*x)
def f(t):
    return t+ 1996.5
#Definimos el rango de la variable t1 y el intervalo en el que cambia
t1 = np.arange(0,25,1)
# Graficamos la variable t1 contra la funcion f(t1)
plt.plot (t1, f(t1),'b', t1, f(t1),'rD')
#Le colocamos una leyenda a cada eje
plt.xlabel('Edad')
plt.ylabel('anios')
#Ajustamos los ejes
plt.axis([0,25, 1995,2020])
#Guarda la grafica en el formato png
plt.savefig('Rodrigo.png')
plt.show()
