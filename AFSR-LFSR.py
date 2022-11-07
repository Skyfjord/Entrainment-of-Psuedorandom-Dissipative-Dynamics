import math
import random
import matplotlib.pyplot as plt

N=12
a=[1,0,0,1,0,1,0,0,0,0,0,1]

if input("Manual inputs? : ")[0] not in ["n","N"]:
    N=int(input("Enter value of N : "))
    a=""
    while len(a.lstrip("0"))!=N:
        a=input("Enter a_i as a string : ")
    a=[int(a[i]) for i in range(len(a))]


xlfsr=[random.choice([0,1]) for _ in range(N)]
xafsr=[xlfsr[i]+(0.2*random.random()-0.1) for i in range(N)]

for _ in range(50):
    s=sum([ a[i]*xafsr[len(xafsr)-i-1] for i in range(N)] )
    xafsr.append((1-math.cos(math.pi*s))/2)

for _ in range(50):
    s=sum([ a[i]*xlfsr[len(xlfsr)-i-1] for i in range(N)] )
    xlfsr.append(s%2)

plt.plot(xafsr,color='black',label='AFSR', marker='+',markerfacecolor='None')
plt.plot(xlfsr,color='red',label='LFSR',linestyle='None',marker='o',markerfacecolor='None')
plt.legend(loc='upper right')

plt.show()
