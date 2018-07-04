#!/bin/python
import math

def Problem13():
	fh = open("resources/problem13input.txt")
	sum = 0
	for line in fh:
		sum = sum + int(line[0:11])
	sumString = "{}".format(sum)
	return(int(sumString[0:10]))

if __name__ == "__main__":
	Problem13()	

