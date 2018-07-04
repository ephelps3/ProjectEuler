#!/bin/python
#The following iterative sequence is defined for the set of positive integers:
#
#n : n/2 (n is even)
#n : 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 : 40 : 20 : 10 : 5 : 16 : 8 : 4 : 2 : 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?

import math

def Problem14():
	nums = range(500000, 1000000)
	hwm = 0
	hwmNum = 0
	for num in nums:
		level = 1;
		numEx = num
		while numEx != 1:
			numEx, level = sequence(numEx, level)
		if level > hwm:
			hwm = level	
			hwmNum = num

	return hwmNum		
def sequence(num, level):
	if num % 2 == 0:
		return num/2, level + 1
	else:
		return (3 * num)+1, level + 1	

if __name__ == "__main__":
	Problem14()	

