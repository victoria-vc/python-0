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