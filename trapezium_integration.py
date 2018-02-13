#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alfredo Hernández <aldomann.designs@gmail.com>

from random import random
from math import *
print "Which integration method do you want to use?"
method = raw_input("Enter T for trapezium, M for Monte Carlo: ").upper()

def function(x):
		""" Evaluates the function we want to integrate """
		# value =  sqrt(1 - x ** 2)
		value = 1/(1 + x**3)
		return value

if method == "T":
	print "This program integrates f(x) in [a,b]."
	A = float(raw_input("Enter tha value of 'a': "))
	B = float(raw_input("Enter tha value of 'b': "))
	if A < B:
		N = int(raw_input("How many interations do you want to do? "))
		tolerance = int(raw_input("How many exact decimals do you want in your result? "))
		result = [0]
		for key in range(1,N+1):
			sum_value = 0
			H = (B - A)/key
			for subkey in range(1,key):
				sum_value += function(A + H*subkey)
			result.append(H/2 * (function(A) + function(B) + 2*sum_value))
			print "Result %i ~ %.*f" % (key, tolerance, result[key])
			if abs(result[key] - result[key-1]) < pow(10, -tolerance):
				print "lol" + str(key)
	else:
		print "Sorry, 'a' must be strictly smaller than 'b'. Try again."

elif method == "M":
	#print "This program tries to calculate the value of Pi using the Monte Carlo method."

	points = int(raw_input("How many points do you want to generate?: "))
	x_lenght = 4
	y_lenght = 1
	AREA = x_lenght * y_lenght
	point_x = [x_lenght * random() for i in range(0,points)]
	point_y = [y_lenght * random() for i in range(0,points)]
	inside = 0

	for i in range(0, points):
		if point_y[i] < function(point_x[i]):
			inside += 1
	result = inside * AREA / float(points)

	print "Result ~ %.20f" % result

else:
	print "Sorry, try again."
