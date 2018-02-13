#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alfredo Hernández <aldomann.designs@gmail.com>
#
# Description:
#	The idea of this method is using the fact that the function
#	n^(1/n) has a maximum at n = e - 1. The algorithm sweeps the
#	n domain until it reaches the maximum of the function.

TOLERANCE = 9
STEP = pow(10,-TOLERANCE)
# The maximum of n^(1/n) is reached in ceiling( (e-1) * 1 / STEP )
MAX_ITER = int(2/STEP)

def calc_root(number):
	""" Calculates n^(1/n). This function has a maximum at n = e - 1 """
	return pow(number, 1/number)

count = 0
value = 1
for i in range(1, MAX_ITER):
	count += 1
	# Update values
	value_old = value
	value = calc_root(1 + i*STEP)

	# Stop when the maximum has been reached
	if value <= value_old:
		max_e = 1 + i*STEP
		break

print("Solution found in", count, "iterations:", "e = ", max_e)
