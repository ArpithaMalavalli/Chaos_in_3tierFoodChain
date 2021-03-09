import math 
from numpy import arange
import matplotlib.pyplot as plt

#x'=y
#y'= -wsq*x =F(x,y,t)

def fi(u,a,b):
    return (a*u)/(1+ b*u)
def F(x, y, z, t):
    return x*(1-x) - fi(x,5.0,3.0)*y
def G(x,y,z,t):
    return fi(x,5.0,3.0)*y-fi(y,0.1,2.0)*z-0.4*y
def L(x,y,z,t):
    return  fi(y,0.1,2.0)*z -0.01*y


a = 0.0
b = 1000.0
N =100000
h = (b-a)/N

# time series
tpoints= arange(a,b,h)

#initial conditions - all combinations in x_list and y_list
x_l=[0.77,0.78]

#RK4



plt.figure()

for x in x_l:
    xpoints=[]
    ypoints=[]
    zpoints=[]
    y=0.15
    z=9.8
    for t in tpoints:
        xpoints.append(x)
        ypoints.append(y)
        zpoints.append(z)
        
        m1 = h*G(x,y,z,t)  #function one
        k1 = h*F(x,y,z,t)
        l1 = h*L(x,y,z,t) #(function 2

        m2 = h*G(x+0.5*m1, y+0.5*k1,z+0.5*l1,t+0.5*h)
        k2 = h*F(x+0.5*m1, y+0.5*k1,z+0.5*l1, t+0.5*h)
        l2 = h*L(x+0.5*m1, y+0.5*k1,z+0.5*l1, t+0.5*h)

        m3 = h*G(x+0.5*m2, y+0.5*k2,z+0.5*l2, t+0.5*h)
        k3 = h*F(x+0.5*m2, y+0.5*k2,z+0.5*l2, t+0.5*h)
        l3 = h*L(x+0.5*m2, y+0.5*k2,z+0.5*l2, t+0.5*h)

        m4 = h*G(x+m3, y+k3,z+l3, t+h)
        k4 = h*F(x+m3, y+k3,z+l3, t+h)
        l4 = h*L(x+m3, y+k3,z+l3, t+h)

        x += (m1 + 2*m2 + 2*m3 + m4)/6
        y += (k1 + 2*k2 + 2*k3 + k4)/6
        z += (l1 + 2*l2 + 2*l3 + l4)/6

    plt.xlabel('time ( 1 unit = 10 time steps)', fontsize = 16)
    plt.ylabel('x', fontsize = 16)
    plt.plot(tpoints[3000:9999], xpoints[3000:9999])

plt.grid()
plt.title("x vs t")
plt.show()
'''
 j1 = h*A(x(i),y(i),z(i));
    k1 = h*C(x(i),y(i),z(i));
    l1 = h*L(x(i),y(i),z(i));
    
    j2 = h*A(x(i)+j1/2,y(i)+k1/2,z(i)+l1/2,t(i)+h/2);
    k2 = h*C(x(i)+j1/2,y(i)+k1/2,z(i)+l1/2,t(i)+h/2);    
    l2 = h*L(x(i)+j1/2,y(i)+k1/2,z(i)+l1/2,t(i)+h/2);
    
    j3 = h*A(x(i)+j2/2,y(i)+k2/2,z(i)+l2/2,t(i)+h/2);
    k3 = h*C(x(i)+j2/2,y(i)+k2/2,z(i)+l2/2,t(i)+h/2);
    l3 = h*L(x(i)+j2/2,y(i)+k2/2,z(i)+l2/2,t(i)+h/2);
    
    j4 = h*A(x(i)+j3,y(i)+k3,z(i)+l3,t(i)+h);
    k4 = h*C(x(i)+j3,y(i)+k3,z(i)+l3,t(i)+h);
    l4 = h*L(x(i)+j3,y(i)+k3,z(i)+l3,t(i)+h);
    
    x(i+1)= x(i)+(h/6)*(j1+2*j2+2*j3*j4);
    y(i+1) = y(i)+(h/6)*(k1+2*k2+2*k3*k4);
    z(i+1) = z(i)+(h/6)*(l1+2*l2+2*l3*l4);
'''