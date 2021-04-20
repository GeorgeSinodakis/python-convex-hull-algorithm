import matplotlib.pyplot as plt
import matplotlib.lines as lines
import math as m
import random
import convex_hull
import k_means

points = set()

while len(points)!= 2000:
	x = random.randint(0, 100)
	y = random.randint(0, 100)
	if (x<20 and 80>y>20) or (y>=80) or(x>=80 and 80>y>20) or (40<x<60 and y<60):
		points.add((x, y))

teams = k_means.clustering(points, 2)

for i in range(len(teams)):
	for p in teams[i]:
	    plt.plot(p[0], p[1], 'rbkym'[i] +'.')

plt.axis('square')
plt.show()
