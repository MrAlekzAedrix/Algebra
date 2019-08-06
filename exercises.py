#Ej 2

from numpy import *
from lineal import *
a=array([[1/2, 1/3, 1/4, 1/5], [2/3, 1/2, 5/3, 2/6], [3/4,3/5,1/2, 3/7], [4/5, 4/6, 4/7, 1/2]], float)
b=array([[2],[4],[6],[8]],float)

print(gaussjordan(a,b))


#Ej3

a=array( [ [1,1.1051,1,1 ], [4,1.2214,2,1], [16,1.4918,4,1], [25,1.6487,5,1] ], float)
b=array( [ [3], [5], [2], [4] ], float)

print(gaussjordan2(a,b))



#Ej4
a=array( [ [1,1/2,1/3 ], [1/4,1/5,1/6], [1/7,1/8,1/9] ],float)
b=array( [ [4], [5], [6] ],float)

a1=array( [ [0.9,1/2,1/3 ], [1/4,1/5,1/6], [1/7,1/8,1/9] ],float)

x=array( [ [121],[-666],[648] ], float)

print(gaussjordan2(a,b))
print()
print(inverse(a,b))

print(gaussjordan2(a1,b))

print(jacobi1(a,b,x,0.01,50))