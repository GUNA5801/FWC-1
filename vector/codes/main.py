import numpy as np
import math as m
import random as r
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys

#local imports
#from funcs import *


#from params import *


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


#Intersection of two lines
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  print(type(N))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
  return P

#Foot of the Perpendicular
def perp_foot(n,cn,P):
  m = omat@n
  N=np.block([[n],[m]])
  p = np.zeros(2)
  p[0] = cn
  p[1] = m@P
  #Intersection
  x_0=np.linalg.inv(N)@p
  return x_0

#Reflection
def reflect(n,c,P):

  D = P+2*(c-n@P)/(LA.norm(n)**2)*n
  return D


#if using termux
import subprocess
import shlex
#end if


#input parameters
a=4                  #length of base (AB)
b=2                     #length of side (AD)
theta = np.pi/3         #angle between AB & AD
A = np.array([0,0])     #Vertex A
B = np.array([a,0])
C = b*np.array([(a/b)+(np.cos(theta)),(np.sin(theta))])
D = b*np.array([(np.cos(theta)),(np.sin(theta))])

P = b*np.array([(np.cos(r.uniform(0,theta))),(np.sin(r.uniform(0,theta)))])


A1 = LA.norm(np.cross(A-D,A-P))/2   #Area of triangle APD
A2 = LA.norm(np.cross(B-C,P-B))/2   #Area of triangle PBC

A3 = LA.norm(np.cross(A-B,B-P))/2   #Area of triangle APB
A4 = LA.norm(np.cross(C-D,D-P))/2   #Area of triangle PCD

print(A1+A2)

APa = LA.norm(np.cross(A-D,A-B))    #Area of || ABCD
print(APa)

if (A3+A4 == APa/2):
    print('Areas are equal')
else:
    print('Areas are not equal')

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

x_PA = line_gen(P,A)
x_PB = line_gen(P,B)
x_PC = line_gen(P,C)
x_PD = line_gen(P,D)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_DA[0,:],x_DA[1,:])

plt.plot(x_PA[0,:],x_PA[1,:])
plt.plot(x_PB[0,:],x_PB[1,:])
plt.plot(x_PC[0,:],x_PC[1,:])
plt.plot(x_PD[0,:],x_PD[1,:])


#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,                                   # this is the text
                 (tri_coords[0,i], tri_coords[1,i]),    # this is the point to label
                 textcoords="offset points",            # how to position the text
                 xytext=(5,-15),                      # distance from text to points (x,y)
                 ha='left')                           # horizontal alignment can be left, right or center

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
#plt.legend(loc='best')
plt.grid()
plt.axis('equal')

#if using termux
plt.savefig('fig.pdf')
#subprocess.run(shlex.split("termux-open '/sdcard/FWC/Matrices/Line/linep.pdf'")) 
#else
#plt.show()

