#!/bin/python

# What is the greatest product of four adjacent numbers 
# in the same direction (up, down, left, right, or diagonally) 
# in the 20x20 grid?

row1 =  [8, 02, 22, 97, 38, 15, 0, 40, 0, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91, 8]
row2 =  [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
row3 =  [81 ,49 ,31 ,73 ,55 ,79 ,14 ,29 ,93 ,71 ,40 ,67 ,53 ,88 ,30 ,03 ,49 ,13 ,36 ,65]
row4 =  [52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91]
row5 =  [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
row6 =  [24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
row7 =  [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
row8 =  [67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
row9 =  [24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
row10 = [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
row11 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14, 9, 53, 56, 92]
row12 = [16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
row13 = [86, 56, 0, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
row14 = [19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40]
row15 = [04, 52, 8, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
row16 = [88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
row17 = [04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
row18 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16]
row19 = [20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54]
row20 = [01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 01, 89, 19, 67, 48]

grid = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15, row16, row17, row18, row19, row20]

def main():
	top = 0
	coords = (0, 0)

	for r in range(0,20):
		for c in range(0,20):
			tempDown = getDown(r, c)
			if tempDown > top: top = tempDown
			tempUp = getUp(r, c)
			if tempUp > top: top = tempUp
			tempRight = getRight(r, c)
			if tempRight > top: top = tempRight
			tempDiag1 = getDiagSE(r, c)
			if tempDiag1 > top: top = tempDiag1
			tempDiag2 = getDiagSW(r, c)
			if tempDiag2 > top: top = tempDiag2
			tempDiag3 = getDiagNE(r, c)
			if tempDiag3 > top: top = tempDiag3
			tempDiag4 = getDiagNW(r, c)
			if tempDiag4 > top: top = tempDiag4

	print("Final Top: {}".format(top))

def getDown(r, c):
	current = grid[r][c]
	count = 0
	while c < 19 and count < 3:
		count = count + 1
		c = c + 1
		current = current * grid[r][c]			
	return current

def getUp(r, c):
	current = grid[r][c]
	count = 0
	while r >= 1 and count < 3:
		count = count + 1
		r = r - 1
		current = current * grid[r][c]			
	return current
def getRight(r, c):
	current = grid[r][c]
	count = 0
	while r < 19 and count < 3:
		count = count + 1
		r = r + 1
		current = current * grid[r][c]			
	return current

def getDiagSE(r, c):
	current = grid[r][c]
	count = 0
	while r < 19 and c < 19 and count < 3:
		count = count + 1
		r = r + 1
		c = c + 1
		current = current * grid[r][c]			
	return current

def getDiagSW(r, c):
	current = grid[r][c]
	count = 0
	while r < 19 and c >= 1 and count < 3:
		count = count + 1
		r = r + 1
		c = c - 1
		current = current * grid[r][c]			
	return current

def getDiagNE(r, c):
	current = grid[r][c]
	count = 0
	while r >= 1 and c < 19 and count < 3:
		count = count + 1
		r = r - 1
		c = c + 1
		current = current * grid[r][c]			
	return current

def getDiagNW(r, c):
	current = grid[r][c]
	count = 0
	while r >= 1 and c >= 1 and count < 3:
		count = count + 1
		r = r - 1
		c = c - 1
		current = current * grid[r][c]			
	return current


if __name__ == "__main__":
	main()

