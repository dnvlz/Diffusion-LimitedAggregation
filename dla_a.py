from numpy import empty,arange,array
from random import randrange,random
from pylab import plot,show,grid
from vpython import sphere,rate,vector,curve,color

L = 101
M = L//2

curve(pos=[vector(-M,-M,0),vector(-M,M,0),vector(M,M,0),vector(M,-M,0),vector(-M,-M,0)], color=color.red)

anchored = []
anchored_coordinates = []
count = 0

while [0,0] not in anchored_coordinates:
    anchored.append(sphere(pos=vector(0,0,0),radius=0.6))
    m = False
    i = j = 0
    while m == False:
        rate(1000)
        i0,j0 = i,j
        if random() < 0.5:
            i += randrange(-1,2,2)
        else:
            j += randrange(-1,2,2)
        anchored[count].pos = vector(i,j,0)
        if [i,j] in anchored_coordinates:
            anchored_coordinates.append([i0,j0])
            anchored[count].pos = vector(i0,j0,0)
            m = True
        elif (abs(i) == M or abs(j) == M):
            anchored_coordinates.append([i,j])
            anchored[count].pos = vector(i,j,0)
            m = True
    count += 1