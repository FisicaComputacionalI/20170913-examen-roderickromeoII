import numpy as np
import matplotlib.pyplot as plt
#Definimos el rango de las variable y el intervalo en el que cambian
t1 = np.arange(0,25,1)
t2 = np.arange(0,2,0.001)
#Crea el grupo de graficas
plt.figure(1)
#Crea el lienzo con dos reglones, una columna y entra a la primera seccion de esta division
plt.subplot(211)
#Grafica la variable t1 contra la funcion f(t1) y grafica la variable t2 contra la funcion f(t)
plt.plot(t1, t1+1996.5, 'r', t2, np.sin(2*np.pi*t2)+ 2015, 'g')
#entra a la segunda seccion del lienzo dividido
plt.subplot(212)
#grafica la variable t2 contra la funcion cos*(2pi*x)
plt.plot(t2, np.sin(2*np.pi*t2)+ 2015, 'b', t2, np.sin(2*np.pi*t2)+ 2015, 'gD')
#Guarda la grafica
plt.savefig('double_funtion.png')
#Muestra la grafica
plt.show()
