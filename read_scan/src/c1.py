import matplotlib.pyplot as plt
import math

f = open('s1.txt','r')
f2 = open('s2.txt','r')

dist_inc = 0.0384

c = f.readline()
target = c.split('(')[1:]
print(len(target))
result=list()


for i in range(len(target)):
	target[i]=target[i][:-1]
	result.append(list(map(float, target[i].split(','))))

x=[]
y=[]

dist=0
angle=0
ang_inc = float(f2.readline())

for i in result:
	for j in i:
		x.append(j*math.cos(angle)-dist)
		y.append(j*math.sin(angle))
		angle+=ang_inc
	dist+=dist_inc
	angle=0

plt.scatter(x,y,c='b',s=2)
plt.show()

f.close()
f2.close()
