#!/bin/python
import math

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def Problem3():
	primeList=[]
	num = 600851475143
	print("Testing Primality")
	for x in range(2, num/1000): 
		if num%x is 0:
			if is_prime(x):
				primeList.append(x)
	largest = max(primeList)
	return(largest)
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    i = 3
    while i < n/2:
	if n % i == 0:
	    print("Returning False: {} divides by {}".format(n, i))
	    return False
	i = i + 2
    print("RETURNING TRUE FOR {}".format(n))
    return True
   # sqr = int(math.sqrt(n)) + 1
   # for divisor in range(3, sqr, 2):
   #     if n%divisor == 0:
   #         return False
   # return True

if __name__ == "__main__":
	Problem3()

