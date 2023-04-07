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
ret = libconversor.conversor(3.0, 4.0) 
if ret > 0:
    print ("\n")
    print ("$$$$$$$$$$$$$$$$ En wrapper python $$$$$$$$$$$$$$$")
    print ("El valor retornado es " + str(ret))  
    print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")