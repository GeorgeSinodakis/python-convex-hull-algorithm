import matplotlib.pyplot as plt 
import math as m
import random

#decorator for the atan2 mapping 0->pi and 0->-pi to 0->2*pi
def my_atan(y, x):
	if m.atan2(y, x) >=0:
		return m.atan2(y, x)
	else:
		return 2 * m.pi + m.atan2(y, x)

#axis rotation and offset transformation of point
def change_origin(point, angle, offset):
	x =  (point[0] - offset[0])*m.cos(angle) + (point[1] - offset[1])*m.sin(angle)
	y = -(point[0] - offset[0])*m.sin(angle) + (point[1] - offset[1])*m.cos(angle)
	return [x, y]

#find the distance between two points
def distance(a, b):
	return m.sqrt((a[0] - b[0])**2+(a[1] - b[1])**2)

def mean_of_points(points):
	x = 0
	y = 0
	for p in points:
		x += p[0]
		y += p[1]
	return [x / len(points), y / len(points)]

def transform_point(center, p_ref, p_target):
	offset = [p_ref[0], p_ref[1]]
	angle = my_atan(p_ref[1] - center[1], p_ref[0] - center[0])
	return change_origin(p_target, angle, offset)

def find_the_angle(center, p_ref, p_target):
	if p_ref == p_target:
		return 2 * m.pi 
	[x, y] = transform_point(center, p_ref, p_target)
	return my_atan(y, x)

def perimeter(points):
	out_points = []

	#find the center of the points
	center_p = mean_of_points(points)

	#find the point that has the maximum distance from the average of the points
	out_points.append(max(points, key = lambda p: distance(center_p, p)))

	while True:
		minp = min(points, key = lambda p: find_the_angle(center_p, out_points[-1], p))
		if minp in out_points:
			return out_points	
		out_points.append(minp)

	


