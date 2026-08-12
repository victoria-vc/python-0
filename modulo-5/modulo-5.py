## -------------- Parte 01 del modulo: "Numpy 1D y Arreglos" -------------- ##
# Numpy es una biblioteca para computación científica. Proporciona estructuras de datos 
# de alto rendimiento y herramientas para trabajar con arreglos multidimensionales
import numpy as np # Importamos la biblioteca

# Arreglo
# Un arreglo es similar a una lista
# Generalmente tiene un tamaño fijo y elementos con el mismo tipo de dato
arreglo = ["elemento1", "elemento2", "elemento3", 4]
# pos           0             1           2       3
# arreglo[0] = "elemento1"
# arreglo[3] = 4

# Convertir una lista en un arreglo
lista = [1, 2, 3, 4, 5, 6]
array = np.array(lista)

print(type(lista))
# Imprime: <class 'list'>

print(type(array))
# Imprime: <class 'numpy.ndarray'>

# Atributos básicos de Arreglos
# Size: cantidad de elementos de un arreglo
print(array.size) # Imprime: 6

# Ndim: representa el número de dimensiones de un arreglo
print(array.ndim) # Imprime: 1

# Shape: tupla de enteros que indica el tamaño del arreglo en cada dimensión
print(array.shape) # Imprime: (6,)

# Indexación y Slicing
# Cambiar valores
array[0] = 2
print(array) # Imprime: [2 2 3 4 5 6]

# Recortar valores
nuevo_array = array[1:4]
print("Nuevo array recortado: " + str(nuevo_array))
# Imprime "Nuevo array recortado: [2 3 4]"
# Igual que en listas, no se cuenta el último elemento correspondiente al índice
# Si lo contaramos, seria: [2, 3, 4, 5] 
# Pero es: [2, 3, 4]

# Asignar valores
array[4:6] = 1000, 2000
print(array)
# Imprime: [2 2 3 4 1000 2000]

# Operaciones básicas
# Estas operaciones con computacionalmente más rápidas y requieren menos memoria en Numpy
# en comparación con Python normal

# Suma de arreglos (vectores)
u = np.array([1,0])
v = np.array([0,1])
z = u + v
# z = np.array([1,1])

# Resta de arreglos (vectores)
u = np.array([1,0])
v = np.array([0,1])
z = u - v
# z = np.array([1,-1])

# Multiplicación de arreglos con un escalar
y = np.array([10, 20])
w = 2 * y
# w = np.array([20, 40])

# Multiplicación de dos arreglos
a1 = np.array([2,4])
a2 = np.array([4,4])
producto = a1 * a2
# producto = np.array([8, 16])

# Producto punto
a1 = np.array([2,4])
a2 = np.array([4,4])
producto = np.dot(a1, a2) # Función que nos da Numpy
# np.dot(a1, a2) hace:
# a1[0] * a2[0] + a1[1] * a2[1] (producto punto)

# Sumar al arreglo 
# Propiedad que se conoce como "broadcasting"
arreglo = np.array([1, 3])
arreglo = arreglo + 1
# arreglo = np.array([2, 4])

# Funciones universales
# Calcular el valor promedio de los elementos de un arreglo
promedio_arreglo = arreglo.mean()
print("El promedio del arreglo es: " + str(promedio_arreglo))
# Imprime: El promedio del arreglo es: 3.0

# Encontrar el valor máximo
maximo = arreglo.max()
print("El valor máximo del arreglo es: " + str(maximo))
# Imprime: El valor máximo del arreglo es: 4

# Acceder al número pi
np.pi

# Crear un arreglo de radianes
x = np.array([0, np.pi/2, np.pi])

# Aplicar la función seno al arreglo x
y = np.sin(x)

# Linspace
# Devuelve números distribuidos uniformemente sobre un intervalo especificado
# np.linspace(-2, 2, num=5)
# -2   -1   0   1   2
# Número de inicio: -2
# Número de fin: 2
# Número de elementos: 5
# Diferencia entre elementos/muestras: 1
# ----
# np.linspace(-2, 2, num=9)
# -2   -1.75 -1.5 -1.25 -1   0   1   1.25 1.5 1.75 2
# Número de inicio: -2
# Número de fin: 2
# Número de elementos: 9
# Diferencia entre elementos/muestras: 0.5
## -------------- Parte 01 del modulo: "Numpy 1D y Arreglos" -------------- ##