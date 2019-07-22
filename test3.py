from lineal import *
from numpy import *
#Fila
a=array([[4, 2, 5], [2, 5, 8], [2,4,3]], float)
#print(a)
#print("")

#Definición del vector constantes
#Columna
b=array([[18], [27.3], [16.2]], float)
#print(b)
#print("")

print (gauss(a,b))