## -------------- Parte 01 del modulo: "Numpy 1D y Arreglos" -------------- ##
import numpy as np
import matplotlib.pyplot as plt
# matplotlib es una biblioteca completa de gráficos
# pyplot es la parte de matplotlib para manejar gráficos

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y) # plot() grafica o traza
plt.show() # show() muestra lo graficado
## -------------- Parte 01 del modulo: "Numpy 1D y Arreglos" -------------- ##