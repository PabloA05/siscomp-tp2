# Importamos la librería ctypes
import ctypes

# Cargamos la libreria 
libconversor = ctypes.CDLL('./libconversor.so')

# Definimos los tipos de los argumentos de la función conversor
libconversor.conversor.argtypes = (ctypes.c_float,ctypes.c_float,)

# Definimos el tipo del retorno de la función conversor
libconversor.conversor.restype = ctypes.c_float

# Creamos nuestra función conversor en Python
# hace de Wrapper para llamar a la función de C
print ("> llamando a convesor desde python\n")
ret = libconversor.conversor(3.0, 4.0) 
if ret > 0:
    print ("\n> El valor retornado de conversor.c es " + str(round(ret,3)))  

print ("\n-----------\n")

print ("> llamando a convesor desde python con -3.0 y 4.0\n")
ret = libconversor.conversor(-3.0, 4.0) 
if ret > 0:
    print ("\n> El valor retornado de conversor.c es " + str(round(ret,3)))  