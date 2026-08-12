## -------------- Parte 01 del modulo: "Leyendo archivos con Open" -------------- ##
# nombre_archivo = open("ruta", "modo_de_acceso")
# Modo de acceso:
# w: write
# r: read
# file = open("ejemplo.txt", "w")
# Y acá tenemos un objeto de tipo archivo o de tipo file

# Atributo name (obtenemos el nombre del archivo)
# file.name

# Atributo mode (obtenemos el modo del archivo)
# file.mode

# Función (método) close (para cerrar el archivo)
# file.close()

# Declaración with (recomendada)
# Cierra el archivo automáticamente luego de ejecutar el bloque de código
with open("ejemplo1.txt", "r") as file1:
    cosas_del_archivo1 = file1.read() 
    print(cosas_del_archivo1)
    # read() almacena la totalidad del contenido del archivo en la variable 
    # read() almacena en forma de cadena
    # Imprimis lo que se leyo

with open("ejemplo2.txt", "r") as file2:
    cosas_del_archivo2 = file2.readline()
    print(cosas_del_archivo2)
    cosas_del_archivo2 = file2.readline()
    print(cosas_del_archivo2)
    # readline() almacena una línea del archivo en la variable
    # readline() almacena en forma de cadena
    # Imprime: 
    # LÍNEA 1
    # LÍNEA 2

# Bucles en archivos (lectura)
with open("ejemplo1.txt", "r") as file1:
    for line in file1:
        print(line)
        # Imprime todas las líneas del archivo

# Los primeros N caracteres
with open("ejemplo1.txt", "r") as file1:
    primeros_5 = file1.readline(5)
    print(primeros_5)
    # Se imprime "tomas"
## -------------- Parte 01 del modulo: "Leyendo archivos con Open" -------------- ##


## ------------ Parte 02 del modulo: "Escribiendo archivos con Open" ------------ ##
with open("ejemplo3.txt", "w") as file3:
    file3.write("LÍNEA 0\n")
    file3.write("LÍNEA 1\n")

with open("ejemplo3.txt", "r") as file3:
    print(file3.read())
    # Imprime "LÍNEA 0"
    #         "LÍNEA 1"

# Bucles en archivos (escritura)
Lineas = ["LÍNEA 0 \n", "LÍNEA 1 \n", "LÍNEA 2 \n"]
with open("ejemplo3.txt", "w") as file3:
    for linea in Lineas:
        file3.write(linea)

with open("ejemplo3.txt", "r") as file3:
    print(file3.read())
    # Imprime "LÍNEA 0"
    #         "LÍNEA 1"
    #         "LÍNEA 2"
## ------------ Parte 02 del modulo: "Escribiendo archivos con Open" ------------ ##


## -------------- Parte 03 del modulo: "Cargando data con Pandas" --------------- ##
# Pandas
# Pandas es una biblioteca popular para el análisis de datos
# Si importamos pandas, tenemos acceso a gran número de clases y funciones preconstruidas:
# read_csv(), Series(), DataFrame, values, etc.
import pandas as pd
# Escribir pandas todo el rato puede ser tedioso; mejor abreviar
# pd = pandas (lo aclaramos en la importación de pandas)

csv_path = 'file1.csv'
# Un CSV es un tipo de archivo típico utilizado para almacenar datos

data_frame = pd.read_csv(csv_path)
# Un data frame se compone de filas y columnas

data_frame.head()
# Te muestra las primeras 5 filas por defecto
# Podes elegir la cantidad
# data_frame.head(2) (primeras 2)

data_frame.tail()
# Te muestra las últimas 5 filas por defecto
# Podes elegir la cantidad
# data_frame.tail(2) (últimas 2)
# Se puede crear un data frame a partir de un diccionario
Videojuegos = {"Nombre": ["Meccha Chameleon", "GTA 5", "Sims 4", "Minecraft"],
                "Anio": [2026, 2013, 2014, 2009],
                "Tipo": ["Aventura", "Acción", "Simulación", "Construcción"]}

juegos_dataframe = pd.DataFrame(Videojuegos)
# Se forma una tabla con los datos del diccionario Videojuegos

# Acceder a la tabla especificando fila y columna
print(juegos_dataframe.iloc[0, 0]) # iloc para números
print(juegos_dataframe.loc[0, "Anio"]) # loc para nombres
## -------------- Parte 03 del modulo: "Cargando data con Pandas" --------------- ##


## -------------- Parte 04 del modulo: "Guardando data con Pandas" -------------- ##
# Unique
# Supongamos que se tiene un Data Frame con álbumes y su fecha de lanzamiento
# Quiero saber qué fechas de lanzamiento son únicas, es decir, que no se repiten
# Hacemos:
# df["Released"].unique()

# Bool
# Si queremos los álbumes que se lanzaron a partir de 1980
# Hacemos:
# df["Released"] >= 1980
# Podemos colocar esos álbumes en otro DataFrame
# otro_df = df[df["Released"] >= 1980]

# Guardar nuestro Data Frame (método to_csv)
# otro_df.to_csv("albumes80.csv")

## -------------- Parte 04 del modulo: "Guardando data con Pandas" -------------- ##