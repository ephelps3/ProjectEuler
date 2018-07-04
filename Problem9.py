#!/bin/python/

import math
# A Pythagorean triplet is a set of three natural numbers, 
# a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which 
# a + b + c = 1000.
# Find the product abc.

def Problem9():
	sum = 1000
	triples = []

	for a in range(1, 1000):
		for b in range (1, 1000):
			c_squared = (a * a) + (b * b)
			c = math.sqrt(c_squared)
			if a + b + c == 1000:
				#print("FOUND TRIPLET: {} {} {}".format(a, b, c))
				#print("Product = {}".format(a*b*c))
				return(a*b*c)
				exit(1)

if __name__ == "__main__":
	Problem9()
