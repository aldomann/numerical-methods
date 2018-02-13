#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alfredo Hernández <aldomann.designs@gmail.com>

import math
from random import random

gen_numbers = []

print("This program generates a sample of an exponential distribution f(x) = l * exp(-l*x).")
print("The results are saved into a exp-sample.csv file.")

lamda = float(input("What's the value of lambda?: "))
points = int(input("How many numbers do you want to generate?: "))

# Random variable that follows an exponential distribution using Inversion Method
def exp_dist(u):
	x = - 1/lamda * math.log(1 - u)
	return x

# Generate numbers
for key in range(0, points):
	gen_numbers.append(exp_dist(random()))

# Print distribution
with open("exp-sample.csv", "w") as file:
	for key in range(0,points):
		file.write("%f\n" % (gen_numbers[key]))
while not file.closed:
	file.close()
