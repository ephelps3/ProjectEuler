#!/bin/python

# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def Problem5():
	i = 40
	while True:
		result = use_divisors(i)
		if result:
			print(i)
			break
		else:
			i = i+20
	return(i)
def use_divisors (i):
	divisors = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
	    11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

	for k in divisors:
		if i%k != 0:
			return False	
	return True

if __name__ == "__main__":
	Problem5()
