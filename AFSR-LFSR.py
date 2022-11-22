import math
import random
import matplotlib.pyplot as plt
import numpy
import mpld3


N=30
a=[1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0\
    , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0\
    , 0, 0, 0, 0, 1]
mu=1.8
delta=0.2
epsilon=1


def reinitialize():
    global N,a,mu,delta,epsilon
    N=int(input("Enter value of N : "))
    a=""
    while len(a.lstrip("0"))!=N:
        a=input("Enter a_i as a string : ")
    a=[int(a[i]) for i in range(len(a))]
    mu=float(input("Enter value of mu : "))
    delta=float(input("Enter value of delta : "))
    epsilon=float(input("Enter value of epsilon : "))

def randomnumgen(length):
    return [random.uniform(-1,1) for _ in range(length)]

def noisegen(length):
    x=[random.choice([-1,1]) for _ in range(N)]
    for _ in range(length-N):
        s=sum([ a[i]*(1 + x[len(x)-i-1])/2 for i in range(N)] )
        x.append(-math.cos(math.pi*s))
    return x

def modulator(message,noise):
    return [noise[i]*(1 + mu*message[i]) for i in range(len(message))]

def reciever(length,transmitted):
    y=[random.choice([-1,1]) for _ in range(N)]
    for _ in range(length-N):
        s=sum([ a[i]*(1 + y[len(y)-i-1])/2 for i in range(N)] )
        yt=-math.cos(math.pi*s)
        if abs(transmitted[len(y)]) < 1 - delta :#abs( abs( transmitted[len(y)] ) - 1 )>delta : #
            y.append(yt)
        else:
            y.append( (1 - epsilon)*yt + epsilon*(math.copysign(1,transmitted[len(y)])) )
    return y

def decoder(transmitted,noise):
    return [ (transmitted[i]/noise[i] - 1)/mu if noise[i]!=0 else 0 for i in range(len(transmitted))]

if input("Manual inputs? : ")[0] not in ["n","N"]:
    N=int(input("Enter value of N : "))
    a=""
    while len(a.lstrip("0"))!=N:
        a=input("Enter a_i as a string : ")
    a=[int(a[i]) for i in range(len(a))]
    mu=float(input("Enter value of mu : "))
    delta=float(input("Enter value of delta : "))
    epsilon=float(input("Enter value of epsilon : "))

checkmessage=False
l=0
if input("Do you want to enter message")[0]=='y':
    checkmessage=True
    message=list(input("Enter message as list : "))
    l=len(message)
else:   
    l=int(input("Enter noise computation limit : "))
    message=randomnumgen(l)

noisex=noisegen(l)

transmit=modulator(message,noisex)
noisey=reciever(l,transmit)
messager=decoder(transmit,noisey)

if checkmessage:
    print("Recieved message : ",messager)

checkA=True
for i in range(l):
    check=True
    for k in range(N):
        if noisex[i+k]!=noisey[i+k]:
            check=False
            break
    if check:
        print("Locking occurred at ",i)
        checkA=False
        break
if checkA:
    print("Locking failed")

while True:

    lower=int(input("Enter lower limit : "))
    upper=int(input("Enter upper limit : "))

    f,axes=plt.subplots(2)

    xaxis=[i for i in range(lower,upper)]

    axes[0].plot(xaxis,noisex[lower:upper],color='red',label='Generator noise',linestyle='None',marker='o',markerfacecolor='None')
    axes[0].plot(xaxis,noisey[lower:upper],color='orange',label='Receiver noise',linestyle='None',marker='+',markerfacecolor='None')
    axes[0].plot(xaxis,transmit[lower:upper],color='green',label='Transmitted message')
    axes[0].legend(loc="upper right")

    axes[1].plot(xaxis,message[lower:upper],color='blue',label='Message',linewidth=2)
    axes[1].plot(xaxis,messager[lower:upper],color='orange',label='Message Recieved',linestyle='dashed')
    axes[1].legend(loc="upper right")

    mpld3.show()

    if input("Do u want to continue : ")[0] in ["n","N"]:
        break
