#!/bin/python

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 
# 3-digit numbers.

def isPalindrome(n):
	num = str(n)
	reverse = num[::-1]
	#print("%s \t %s"%(num, reverse))
	if num in reverse:
		return True

def Problem4():
	list1 = [1, 0]
	for i in range(100, 999):
		for k in range(100, 999):
			product = i*k
			if isPalindrome(product):
				list1.append(product)
	list1.sort()
	print( list1[-1] )
	return( list1[-1] )

if __name__ == "__main__":
	Problem4()
