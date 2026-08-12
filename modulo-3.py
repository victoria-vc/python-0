## -------------- Parte 01 del modulo: "Condiciones y Branching" -------------- ##
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