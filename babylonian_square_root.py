#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alfredo Hernández <aldomann.designs@gmail.com>

from math import sqrt
from math import isclose

radicand = float(input("Which number do you want to find the square root of? "))
square_guess = float(input("Enter your first guess: "))

MAX_STEPS = int(input("How many steps do you want to try? "))
TOLERANCE = 1e-7

def update_guess(guess):
	return (guess + radicand/guess)/2

print("\nReal value: sqrt({radicand:.3f}) = {sqrt_radicand:.6f}\n".format(radicand = radicand, sqrt_radicand = sqrt(radicand)))

for step in range(MAX_STEPS):
	if step > 0:
		square_guess = update_guess(square_guess)
	print("Guess {step} = {value:.6f}".format(step = str(step + 1).zfill(len(str(MAX_STEPS))), value = square_guess))
	if isclose(square_guess, sqrt(radicand), abs_tol = TOLERANCE):
		print("You've found the square root.")
		break
