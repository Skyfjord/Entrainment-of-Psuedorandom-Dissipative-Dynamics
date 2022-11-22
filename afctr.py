import math
import matplotlib.pyplot as plt
import numpy
import mpld3
from math import cos,acos,pi
from random import random

def theta(x):
    if x>=0:
        return 1
    return 0


dt=0.001
a=[1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0\
    , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0\
    , 0, 0, 0, 0, 1]
N=30
zc=1
A=0.7
eps1=0.01
eps2=1
t=29999
x=[-1+i/30000 for i in range(15000)]
x.extend([1-i/30000 for i  in range(15000)])

while True:
    sum=0
    for i in range(N):
        sum+=a[i]*(1+x[t-(2*i+1)*500])/2
    dx=1-cos(pi*sum)
    dx*=cos(pi*(1+x[t-500])/2)
    dx*=A*theta(cos(2*pi*t/1000)-zc)
    dx+=eps1*(x[t]-x[t]**3)
    x.append(x[t]+dx)
    t+=1
    if t==100000:
        break

plt.plot([i/1000 for i in range(100000)],x[:100000])
plt.show()

# for j in range(100):
#     plt.plot([i/1000 for i in range(10000*j,10000*(j+1))],x[10000*j:10000*(j+1)])
#     plt.show()
