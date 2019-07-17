
from lineal import *
from numpy import *

#Fila
a=array([[4,2,5], [2, 5, 8], [5,4,3]], float)
#print(a)
#print("")

#Definición del vector constantes
#Columna
b=array([[60.7], [92.9], [56.3]], float)
#print(b)
#print("")

print(inverse(a,b))


