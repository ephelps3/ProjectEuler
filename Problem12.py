#!/bin/python
import math
#What is the value of the first triangle number to have over five hundred divisors?

def Problem12():
	nums=list(range(1,1000000))
	divLen = 0
	index = 0
	triangle = 0
	while divLen < 500 and index < len(nums):
		triangle=triangle+nums[index]
		divisors = getDivisors(triangle)
		if divLen < len(divisors):
			divLen = len(divisors)
		index = index + 1
	return(triangle)

def getDivisors(n):
	i=1
	divisors = []
	while i <= int(math.sqrt(n)+1):
		if n%i == 0:
			divisors.append(i)
			if i*i != n:
				divisors.append(n/i)	
		i = i+1
	return divisors

if __name__ == "__main__":
	Problem12()	

