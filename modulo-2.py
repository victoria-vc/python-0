## -------------- Parte 01 del modulo: "Listas y Tuplas" -------------- ##
# Tuplas
# Las tuplas son una secuencia ordenada
# Se expresan como elementos separados por comas dentro de paréntesis
# Son inmutables

tupla = (0, 1, 2, 3)
tupla = ('Tomas', 'CABJ', 22)
#           0       1      2  (posiciones)
#           -3      -2     -1 (posiciones)

type(tupla) # = tuple

tupla[0] # = 'Tomas'
tupla[-3] # = 'Tomas'

# Concatenación de tuplas
tuplaza = tupla + ('Argentina', 'Verde')
# = tuplaza = ('Tomas', "CABJ", 22, 'Argentina', 'Verde')

# Slice de tuplas
tuplita = tupla[0:2] # = ('Tomas', 'CABJ')
otra_tuplita = tuplaza[1:4] # = ('CABJ', 22, 'Argentina')

# Longitud de una tupla
len ('Tomas') # = 5
len(tuplaza) # = 5
len(tuplita) # = 2

# Ordenar una tupla
tupla_desordenada = (2, 6, 9, 1, 4)
tupla_ordenada = sorted(tupla_desordenada) # = [1, 2, 4, 6, 9] (devuelve una nueva tupla ordenada)

# Anidamiento en tuplas (nesting)
tupla_rara = (18, ('Jorgito', 'Tatin', 'Havanna'), 'Alfajores', (200, 600, 800))
# Veáse:       0                1                       2               3

tupla_rara[1] # = ('Jorgito', 'Tatin', 'Havanna') 
# Veáse:                0         1         2
tupla_rara[1][2] # = 'Havanna'

# Listas
# Las listas son una secuencia ordenada
# Son mutables

lista = ["Tomas Emiliano", 22, 2004]
lista_rara = ["Alfajores", ["Guaymallen", "Terrabusi"], (600, 1000), "Kiosco Pingu"]
# En la lista puede haber listas y tuplas
# Los índices para las listas son iguales que para las tuplas

# Operaciones de listas
lista.extend(["CABJ", "Argentina"]) # Acá se agregan los dos elementos por separado
# La lista queda: lista = ["Tomas Emiliano", 22, 2004, "CABJ", "Argentina"]
#                               0             1    2      3         4
lista.append(["CABJ", "Argentina"]) # Acá se agregan como un solo elemento
# La lista queda: lista = ["Tomas Emiliano", 22, 2004, ["CABJ", "Argentina"]]
#                               0             1    2            3

del(lista[0]) # Elimina el primer elemento, en este caso, "Tomas Emiliano"
# La lista queda: lista = [22, 2004, ["CABJ", "Argentina"]]
#                               0    1            2
# Los elementos se reordenan automáticamente

lista_messi = "Vamos Messi".split()
# La lista queda: lista_messi = ["Vamos", "Messi"]

lista_messi = "Vamos, Messi".split(",")
# La lista queda: lista_messi = ["Vamos", "Messi"]

## -------------- Parte 01 del modulo: "Listas y Tuplas" -------------- ##