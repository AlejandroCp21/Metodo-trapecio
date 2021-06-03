#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
#metodo Simpson


# In[ ]:


def f(x):
    return (funcion)


# In[ ]:


n = int(input("Ingresar limite n: "))
a = float(input("ingresar limite a: "))
b = float(input("ingresar limite b: "))
Valor_R=float(input("ingresar valor real de la integral: "))
h = (b-a)/n
par=0
impar=0
if n%2==0:
    for i in range(1,n):
        xi=a+i*h
        if i%2==0:
            par+=f(xi)
        else:
            impar+=f(xi)
    suma1=2*par
    suma2=4*impar
    t=(h/3)*(suma1+suma2)
    
    r=(h/3)*(f(a)+f(b))+t
    error=abs(Valor_R-r)

    print("aproximacion= ",r, "con un error de: ",error)
else: 
    print("n no es par")

