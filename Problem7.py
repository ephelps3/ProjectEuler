#!/bin/python
import math
 # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
primes = [2, 3]

def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def Problem7():
	i=5
	while len(primes) != 10001:
		if is_prime(i):
			primes.append(i)
		i=i+2	

	print(primes[-1])
	return(primes[-1])

if __name__ == "__main__":
	Problem7()
