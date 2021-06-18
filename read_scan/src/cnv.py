import matplotlib.pyplot as plt
from decimal import Decimal
import math


s11 = open('sample.txt','r')
s22 = open('sample2.txt','r')

s1 = s11.readline()
s2 = s22.readline()

samp1 = list(map(float, s1[1:len(s1)-1].split(',')))
samp2 = list(map(float, s2[1:len(s2)-1].split(',')))

print(len(samp1))
print(len(samp2))

x = []
y = []

angle=0
inc=0.024259403348

for i in range(len(samp1)):
	x.append(samp1[i]*math.cos(angle))
	y.append(samp1[i]*math.sin(angle))
	angle+=inc
plt.scatter(x,y,color='r',s=10)
plt.show()


angle=0
for j in range(len(samp2)):
	x.append(samp2[j]*math.cos(angle)-0.5)
	y.append(samp2[j]*math.sin(angle))
	angle+=inc

plt.scatter(x,y,color='b', s=10)
plt.show()

s11.close()
s22.close()

