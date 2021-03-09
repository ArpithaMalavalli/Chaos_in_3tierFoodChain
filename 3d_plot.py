import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math 
from numpy import arange
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

def fi(u,a,b):
    return (a*u)/(1+ b*u)
def F(x, y, z, t,b):
    return x*(1-x) - fi(x,5.0,b)*y
def G(x,y,z,t,b):
    return fi(x,5.0,b)*y-fi(y,0.1,2.0)*z-0.4*y
def L(x,y,z,t):
    return  fi(y,0.1,2.0)*z -0.01*y


a = 0.0
b = 1000.0
N =100000
h = (b-a)/N

# time series
tpoints= arange(a,b,h)

#initial conditions - all combinations in x_list and y_list

#RK4

b_l=arange(2.6,3.2,0.1)

plt.figure()

for b in b_l:
    xpoints=[]
    ypoints=[]
    zpoints=[]
    r=[]
    y=0.15
    z=9.8
    x=0.78
    for t in tpoints:
        xpoints.append(x)
        ypoints.append(y)
        zpoints.append(z)
        r.append(b)
        
        m1 = h*G(x,y,z,t,b)  #function one
        k1 = h*F(x,y,z,t,b)
        l1 = h*L(x,y,z,t) #(function 2

        m2 = h*G(x+0.5*m1, y+0.5*k1,z+0.5*l1,t+0.5*h,b)
        k2 = h*F(x+0.5*m1, y+0.5*k1,z+0.5*l1, t+0.5*h,b)
        l2 = h*L(x+0.5*m1, y+0.5*k1,z+0.5*l1, t+0.5*h)

        m3 = h*G(x+0.5*m2, y+0.5*k2,z+0.5*l2, t+0.5*h,b)
        k3 = h*F(x+0.5*m2, y+0.5*k2,z+0.5*l2, t+0.5*h,b)
        l3 = h*L(x+0.5*m2, y+0.5*k2,z+0.5*l2, t+0.5*h)

        m4 = h*G(x+m3, y+k3,z+l3, t+h,b)
        k4 = h*F(x+m3, y+k3,z+l3, t+h,b)
        l4 = h*L(x+m3, y+k3,z+l3, t+h)

        x += (m1 + 2*m2 + 2*m3 + m4)/6
        y += (k1 + 2*k2 + 2*k3 + k4)/6
        z += (l1 + 2*l2 + 2*l3 + l4)/6

    plt.scatter(r[9000:9999],zpoints[9000:9999])

plt.grid()
plt.title("x vs t")
plt.show()
