#!/bin/python

# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

def Problem6():
	natural_nums = range(1, 101)

	sum = 0
	for i in natural_nums:
		sum = sum + (i*i)

	print("sum of squares: %i"%sum)	

	square = 0
	for i in natural_nums:
		square = square + i
	square = square * square

	print("square of sums: %i"%square)


	print("Difference; {}".format(square - sum))
	return (square - sum)

if __name__ == "__main__":
	Problem6()
