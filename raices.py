import math

#biseccion
def f(x):
    y = x - (math.sin(x))
    return y

print("Root finder 'x-sin(x)' ")
xa = -2
xb = 2
err = 0.0001
xr = (xa+xb)/2.0
i = 1

while abs(f(xr)) > err:
    i = i+1
    xr = (xa+xb)/2.0
    if f(xa) * f(xr) > 0:
        xa = xr
    else:
        xb = xr
print("Number of iteration: ", i)
print("Root: ", xr)

#Newton-Raphson

def f(x):
    return x ** 4 - 10 * (x ** 3) + 3 * (x ** 2) + x + 23

def df(x):
    return 4 * (x ** 3) - 30 * (x ** 2) + 6 * x + 1


i=1
err=0.0001

while i<err:
    i=i+1
    xin= x - (f(x)/df(x))
    if abs(x-xin) < err:    
        x=xin
        print("Root: ", xin)
#print("Root: ", xin)