## -------------- Video 01 del curso: "Primer programa en Python" -------------- ##
print("Hello World!")
## -------------- Video 01 del curso: "Primer programa en Python" -------------- ##


## ------------------------ Video 02 del curso: "Tipos" ------------------------ ##
# 12 : int
# 12.4 : float
# "Tomas 18" : str
# True : bool
# False : bool

type(12)
type(12.4)
type("Tomas 18")
type(True)
type(False)

# Cambiar el tipo de expresión: typecasting
float(2) # => 2.0
int(4.4) # => 4
int('1') # => 1
int('A') # => ValueError: invalid literal for int() with base 10: 'A'
str(1) # => '1'
str(4.4) # => '4.4'
int(True) # => 1
int(False) # => 0
bool(1) # => True
bool(0) # => False
## ------------------------ Video 02 del curso: "Tipos" ------------------------ ##


## ---------------- Video 03 del curso: "Expresiones y Variables" -------------- ##
# Expresiones
# 40 + 20 = 60
# 40 y 20 son operandos (operands)
# los símbolos matemáticos, en este caso la suma, se llaman operadores (operators)
10 + 10
20 - 10
10 * 2
20 / 2
20 // 3 # => con la doble barra (//) el resultado se redondea hacia abajo

# Variables
variable = 10 # le asignamos un valor
variable = 10 + 10 # le asignamos el resultado de una expresión
variable2 = variable / 3 # le asignamos el resultado de variable / 3
type(variable) # => int
type(variable2) # => float

## ---------------- Video 03 del curso: "Expresiones y Variables" -------------- ##


## ---------------- Video 04 del curso: "Operaciones con Strings" -------------- ##
Nombre = "Tomas Emiliano"
# T o m a s  E m i l i a n o
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 (posiciones)
# -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 (posiciones en negativo, no va el 0)
Nombre[2] # = m
Nombre[14] # = o
Nombre[-1] # = o
Nombre[-13] # = T

Nombre[0:5] # = Tomas
Nombre[6:15] # = Emiliano

Nombre[::2] # = T m s   i i a o (se selecciona cada 2 variables)
Nombre[0:5:4] # = T (se devuelve cada segundo valor hasta el índice 4)

# Longitud de una cadena
len(Nombre) # = 15 (devuelve la cantidad de caracteres que tiene la variable)
len("Tomas Emiliano") # = 15

# Concatenación de una cadena
fusion = Nombre + "es el mejor"
# fusion = "Tomas Emiliano es el mejor"

# Multiplicación de cadenas
2 * Nombre # = "Tomas Emiliano Tomas Emiliano"

# Barra invertida con cadenas
Nombre = "Tomas \n Emiliano" # \n es un salto de línea
Nombre = "Tomas \t Emiliano" # \t es un tabulado
Nombre = "Tomas \\ Emiliano" # \\ es \

# Métodos de Strings
NombreEnMayuscula = Nombre.upper() # = "TOMAS EMILIANO"
NombreEnMinuscula = Nombre.lower() # = "tomas emiliano"

NombreReemplazo = Nombre.replace('Tomas', 'Señor') # = "Señor Emiliano"

Nombre.find('Emiliano') # = 6 (devuelve el primer índice de la secuencia)
Nombre.find('To') # = 0  (devuelve el primer índice de la secuencia)

## ---------------- Video 04 del curso: "Operaciones con Strings" -------------- ##