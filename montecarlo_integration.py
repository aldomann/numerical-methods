#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alfredo Hernández <aldomann.designs@gmail.com>

from random import random
from math import sqrt

points = int(input("How many points do you want to generate?: "))
x_lenght = 4
y_lenght = 1
AREA = x_lenght * y_lenght
point_x = [x_lenght * random() for i in range(0,points)]
point_y = [y_lenght * random() for i in range(0,points)]

print("This program tries to calculate the value of Pi using the Monte Carlo method.")

def function(x):
	""" Evaluates the function we want to integrate """
	# value =  sqrt(1 - x ** 2)
	value = 1/(1 + x**3)
	return value

inside = 0
for i in range(0, points):
	if point_y[i] < function(point_x[i]):
		inside += 1

# result = inside * AREA * 4 / float(points)
result = inside * AREA / float(points)

print ("PI ~ %.20f" % result)
print (6.28/(3 * sqrt(3)))
