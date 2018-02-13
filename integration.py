from random import random
from math import *

print("Which integration method do you want to use?")
method = input("Enter T for trapezium, M for Monte Carlo: ").upper()


def function(x):
	""" Evaluates the function we want to integrate """
	value =  sqrt(1 - pow(x, 2))
	value = 1/(1 + pow(x, 3))
	return value

if method == "T":
	print("This program integrates f(x) in [a,b].")
	A = float(input("Enter tha value of 'a': "))
	B = float(input("Enter tha value of 'b': "))
	if A < B:
		N = int(input("How many subintervals do you want to create? "))
		H = (B - A)/N
		sum_value = 0

		for key in range(1, N):
			sum_value += function(A + H*key)

		result = H/2 * (function(A) + function(B) + 2*sum_value)
		print("Result ~ %.12f" % (result))
	else:
		print("Sorry, 'a' must be strictly smaller than 'b'. Try again.")

elif method == "M":
	points = int(input("How many points do you want to generate?: "))
	x_lenght = 4  # TODO: use [a,b]
	y_lenght = 1
	""" y_lenght == maximum of f(x) in [a,b].
		In mathematica: FindMaxValue[f[x], {x, c, a, b}],
		where c is a value in [a,b]
	"""
	AREA = x_lenght * y_lenght
	point_x = [x_lenght * random() for i in range(0, points)]
	point_y = [y_lenght * random() for i in range(0, points)]
	inside = 0

	for i in range(0, points):
		if point_y[i] < function(point_x[i]):
			inside += 1

	result = inside * AREA / float(points)
	print("Result ~ %.12f" % result)

else:
	print("Sorry, try again.")
