#/bin/python

import Problem3
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
def Problem10():
	i = 1 
	sum = 2
	while i < 2000000:
		if Problem3.is_prime(i):
			sum = sum + i	
		i=i+2

	print("Sum: {} ".format(sum))
	return(sum)

if __name__ == "__main__":
	Problem10()
