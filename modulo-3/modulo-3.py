## -------------- Parte 01 del modulo: "Condiciones y Operadores Lógicos" -------------- ##
# Operaciones de comparación
# a = 6 (asignamos valor a una variable)
# a == 6 (queremos saber si "a" es igual a 6)
# "a" es igual a 6, entonces el resultado es True
# a == 120
# "a" es distinto de 120, entonces el resultado es False
# a > número
# a < número
# a >= número
# a <= número
# a != número

# if(a>6):
# print ("a es mayor a 6")

# If Else
a = 8
if (a > 6): 
    print("a es mayor a 6")
else: 
    print("a no es mayor que 6") # si a <= 6

# ElseIf

b = 6
if (b > 6):
    print("b es mayor a 6")
elif(b == 6):
    print ("b es 6")

# Operadores lógicos

# NOT
not(True) # => False
not(False) # => True

# OR
(True or False) # => True
(True or True) # => True
(False or True) # => True
(False or False) # => False

# AND
(True and False) # => False
(True and True) # => True
(False and True) # => False
(False and False) # => False
## -------------- Parte 01 del modulo: "Condiciones y Branching" -------------- ##


## ---------------------- Parte 02 del modulo: "Loops" ------------------------ ##
# Función range
# range(N)
# secuencia: [0, 1, 2, ..., N-1]
# range(4)
# secuencia: [0, 1, 2, 3]
# range(10, 14)
# secuencia: [10, 11, 12, 13]

# Bucle for
Videojuegos = ["Minecraft", "Habbo", "Yoshi Island", "Pacman"]

print("Alguno de los juegos que me gustan son:")
for i in range(0,4):
    print(Videojuegos[i])

# Función enumerate
Colores = ["Verde", "Azul", "Rojo"]

for i, Color in enumerate(Colores): # Se enumera color a color
   print (Color) 

# Bucle while
Precios = [600, 120, 900, 1200, 4000, 700]

print ("Los precios más bajos son:")
i = 0
while(Precios[i] < 1000): # Se ejecuta mientras se cumpla una condición
    print(Precios[i])
    i = i + 1
## ---------------------- Parte 02 del modulo: "Loops" ------------------------ ##


## -------------------- Parte 03 del modulo: "Funciones" ---------------------- ##
# Funciones de Python
rating_programas = [9.0, 6.4, 8.6, 3.9, 6.2, 4.2]
#                   1      2    3   4     4    6
# La función <len> devuelve la cantidad de elementos de una lista
cantidad_programas = len(rating_programas) # = 6

# La función <sum> devuelve la suma de todos los elementos de una lista o tupla
suma_rating = sum(rating_programas) # = 38.3

# La función <sorted> devuelve una lista o tupla ordenada
rating_programas_ordenado = sorted(rating_programas)
# rating_programas_ordenado = [3.9, 4.2, 6.2, 6.4, 8.6, 9.0]

# La función <sort> modifica (ordena) una lista o tupla
rating_programas.sort()
# rating_programas = [3.9, 4.2, 6.2, 6.4, 8.6, 9.0]

# La función <reverse> invierte el orden de los elementos de una lista
rating_programas.reverse()
# rating_programas = [9.0, 8.6, 6.4, 6.2, 4.2, 3.9]

# Definir nuestras propias funciones
# def nombre_función(parámetro_formal):
#     cuerpo_de_la_función
#     return valor_de_retorno

# Definición de la función
def sumar_1(a):
    return a + 1

# Llamado a la función
sumar_1(6)
# Devuelve 7

c = sumar_1(10)
# c será 11

# Parámetros múltiples
def sumar_numeros(a, b):
    return a + b

sumar_numeros(4, 40)
# Devuelve 44

# Función sin retorno
def boca_juniors():
    print("Boca Juniors")

boca_juniors()

# Función que no hace NADA
def nada():
    pass 
# Python no permite una función con cuerpo vacío, así que agregamos pass (no hace nada)

print(nada())
# Imprime "None"

def sumar(*x): # Con "*x", la función puede recibir una cantidad variable de parámetros
    return sum(x)

print(sumar(2,4,6))
# Imprime 12
## -------------------- Parte 03 del modulo: "Funciones" ---------------------- ##


## ----------------- Parte 04 del modulo: "Clases y Objetos" ------------------ ##
# Objetos
# En Python, cada tipo de dato es un objeto
# Cada objeto en Python es una instancia de una clase
# Cada objeto es un tipo
# Un objeto es una instancia de un tipo particular
# Cada objeto tiene un conjunto de funciones llamadas métodos para interactuar con los datos

# Ejemplo
# Cuando creamos un entero (int)
# Object 1: 40
# Object 2: 10
# etc ...
# O cuando creamos una lista
# Object 1: A = [a, b, c, d]
# Object 2: Lista = [20, 40, 60]
# etc ...

# Methods
# Los métodos de una clase o tipo son funciones que cada instancia de esa clase o tipo proporciona
# Es cómo interactúas con el objeto
# Por ejemplo, en rating_programas.sort():
# sort() es un método de la clase (en este caso, listas)
# rating_programas es el nombre del objeto

# Definir clases
# Las clases tienen:
# - Atributos
# - Métodos (funciones)

class Circulo(object):

    # Atributos de la clase
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color
    # Métodos de la clase
    def cambiar_radio(self,nuevo_radio):
        self.radio = nuevo_radio
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

class Rectangulo(object):

    # Atributos de la clase
    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        self.color = color
    # Métodos de la clase
    def calcular_area(self):
        return self.base * self.altura
    
# La función <init> es un constructor, le dice a Python que estás creando una nueva clase
# El parámetro "self" se refiere a la instancia recién creada de la clase

# Crear un objeto de la clase Circulo
CirculoVerde = Circulo(10, "verde")

# Crear un objeto de la clase Rectangulo
RectanguloAzul = Rectangulo(2, 4, "azul")

# Cambiar valores
CirculoVerde.color = "azul"
RectanguloAzul.base = 3

# Usar métodos
CirculoVerde.cambiar_color("rojo")
RectanguloAzul.calcular_area() # Devuelve 12

# Función dir
# Es útil para obtener la lista de datos y métodos asociados a una clase
# El objeto que nos interesa se pasa como argumento
print(dir(CirculoVerde))
# Imprime: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', '__weakref__', 'cambiar_color', 'cambiar_radio', 'color', 'radio']

print(dir(RectanguloAzul))
# Imprime: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
#  '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', '__weakref__', 'altura', 'base', 'calcular_area', 'color']

# Solo nos importan los atributos que parecen normales y tienen sentido, lo demás lo ignoramos

## ----------------- Parte 04 del modulo: "Clases y Objetos" ------------------ ##