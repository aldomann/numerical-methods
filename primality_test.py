#!/usr/bin/python
# Author: Alfredo Hernández <aldomann.designs>

print("This programs tests if a number is prime using trial division.")
number = int(input("Choose a number: "))

def is_prime(x):
	for i in range(2, int(x ** 0.5) + 1 ):
		if x % i == 0:
			return False
	else:
		return True

print(is_prime(number))
