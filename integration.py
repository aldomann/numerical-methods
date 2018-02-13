#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alfredo Hernández <aldomann.designs@gmail.com>

# TODO: The script doesn't work for sure (the functions and evaluations are not well defined).
# Each method must be calculating a different thing.

from random import random
#from math import sqrt

print("Which integration method do you want to use?")
method = input("Enter T for trapezium, M for Monte Carlo: ").upper()

def function(x):
		""" Evaluates the function we want to integrate """
		# value =  sqrt(1 - x ** 2)
		value = 1/(1 + x**3)
		return value

def monte_carlo_int(points):
	x_lenght = 4
	y_lenght = 1
	AREA = x_lenght * y_lenght
	point_x = [x_lenght * random() for i in range(0,points)]
	point_y = [y_lenght * random() for i in range(0,points)]
	inside = 0

	for i in range(0, points):
		if point_y[i] < function(point_x[i]):
			inside += 1

	return(inside * AREA / float(points))

def trapezium_int(a, b, N, TOLERANCE):
	if a < b:
		result = 0
		for key in range(1,N+1):
			sum_value = 0
			result_old = result
			H = (b - a)/key
			for subkey in range(1,key):
				sum_value += function(a + H*subkey)
			result = H/2 * (function(a) + function(b) + 2 * sum_value)
			if abs(result - result_old) < pow(10, -tolerance):
				return(result)


if method == "T":
	print("This program integrates f(x) in [a,b].")
	a = float(input("Enter tha value of 'a': "))
	b = float(input("Enter tha value of 'b': "))
	N = int(input("How many interations do you want to do? "))
	tolerance = int(input("How many exact decimals do you want in your result? "))
	result = trapezium_int(a, b, N, tolerance)
elif method == "M":
	print("This program tries to calculate the value of Pi using the Monte Carlo method.")
	points = int(input("How many points do you want to generate?: "))
	tolerance = int(input("How many exact decimals do you want in your result? "))
	result = monte_carlo_int(points)
else:
	print("Sorry, try again.")

print("Result ~ %.*f" % (tolerance, result))
