#Gauss-Jordan
import numpy as np
def gaussjordan(a,b):
    n=len(b)
    c=np.concatenate([a,b], axis=1) #matriz aumentada
    for e in range (n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t #Normalizar fila e
        for i in range (n):
            if i!=e:
                t=c[i,e]
                for j in range(e, n+1):
                    c[i, j]=c[i, j]-t*c[e,j] #Reducir otras filas
    x=c[:,n]
    return x

#Gauss-Jordan [mod]
def gaussjordan2(a,b):
    n=len(b)
    c=np.concatenate([a,b], axis=1)
    for e in range(n):
        c[e,e:]=c[e,e:]/c[e,e]
        for i in range(n):
            if i!=e:
                c[i, e:]=c[i, e:]-c[i, e]*c[e,e:]
    x=c[:, n]
    return x


#Gauss-Jordan [Inverse]
import numpy as np
def inverse(a,b):
    n=len(b)
    id=np.identity(n)
    c=np.concatenate([a,b], axis=1) #matriz aumentada
    c=np.concatenate([c,id], axis=1)
    for e in range (n):
        t=c[e,e]
        for j in range(e, (2 * n)+1):
            c[e,j]=c[e,j]/t #Normalizar fila e
        for i in range (n):
            if i!=e:
                t=c[i,e]
                for j in range(e, (2 * n)+1):
                    c[i, j]=c[i, j]-t*c[e,j] #Reducir otras filas
    inv=c[:, n+1:]
    x=c[:,n]
    return inv