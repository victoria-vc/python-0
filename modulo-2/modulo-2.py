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


## ----------------- Parte 02 del modulo: "Conjuntos" ----------------- ##
# Los conjuntos (sets) son un tipo de colección

set1 = {1, 2, 3, 4, 4} 
# Los elementos duplicados no cuentan al conjunto final
# set1 en realidad es: set1 = {1, 2, 3, 4}

# Conversión de lista a conjunto
jugadores_lista = ["Tapia", "Di Nenno", "Chingotto", "Sanyo", "Sanyo"]
jugadores_set = set(jugadores_lista)
# jugadores_set = {"Tapia", "Di Nenno", "Chingotto", "Sanyo"}

# Operaciones con conjuntos
jugadores_set.add("Stupaczuk") # Agrega un elemento al conjunto
# jugadores_set = {"Tapia", "Di Nenno", "Chingotto", "Sanyo", "Stupaczuk"}

jugadores_set.remove("Chingotto") # Elimina un elemento del conjunto
# jugadores_set = {"Tapia", "Di Nenno", "Sanyo", "Stupaczuk"}

"Tapia" in jugadores_set # Chequea si un elemento está o no en el conjunto
# Devuelve True o False
# En este caso devuelve True

jugadores_set2 = {"Tapia", "Di Nenno", "Coello"}

jugadores_set3 = jugadores_set & jugadores_set2 # Devuelve la intersección de los dos conjuntos
# jugadores_set3 = {"Tapia", "Di Nenno"}

jugadores_set3 = jugadores_set | jugadores_set2 # Devuelve la unión de los dos conjuntos
# jugadores_set3 = {"Tapia", "Di Nenno", "Chingotto", "Sanyo", "Stupaczuk", "Coello"}

## ----------------- Parte 02 del modulo: "Conjuntos" ------------------ ##


## ----------------- Parte 03 del modulo: "Diccionarios" ------------------ ##
# Los diccionarios son un tipo de colección
# A cada key (clave) le corresponde un valor
# Los valores para cada key pueden ser mutables, inmutables y duplicados

diccionario = {"key1": 60, "key2": 20, "key3": "UTN", "key4": [4,4,4], "key5": ("B", "O")}

# Ejemplo más entendible:
diccionario = {
    "nombre": "Tomas",
    "edad": 22,
    "anio": 2004,
    "club": "CABJ",
    "pais": "Argentina"
}
# Usando la clave diccionario["nombre"] nos devuelve el valor "Tomas"
# Usando la clave diccionario["anio"] nos vevuelve el valor 2004

# Agregar nueva entrada al diccionario
diccionario["color favorito"] = "Verde"
# Así, el diccionario queda:
# diccionario = {
#     "nombre": "Tomas",
#     "edad": 22,
#     "anio": 2004,
#     "club": "CABJ",
#     "pais": "Argentina",
#     "color favorito": "Verde"
# } 

# Borrar una entrada del diccionario
del(diccionario["edad"])

# Verificar si algún elemento está en el diccionario
"pais" in diccionario
"color favorito" in diccionario
# Devuelve True o False

# Obtener todas las claves del diccionario
diccionario.keys()

# Obtener todos los valores del diccionario
diccionario.values()
## ----------------- Parte 03 del modulo: "Diccionarios" ------------------ ##