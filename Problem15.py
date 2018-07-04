#!/bin/python

# Starting in the top left corner of a 2x2 grid, 
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

grid= [[0 for x in range(20)] for y in range(20)] 
index = 0
row = 0	
while row < 20:
	col = 0
	while col < 20:
		grid[row][col] = index
		index = index + 1
		col = col + 1
	row = row + 1

origin = grid[0][0]
goal = grid[19][19]

def Problem15():
	print("Problem15")
		
	for row in grid:
		print(row)

	print(isValidMove(0,0,0,1))
	print(isValidMove(0,1,0,1))
	print(isValidMove(0,0,1,0))
	print(isValidMove(1,0,2,1))

def isValidMove(srcRow, srcCol, dstRow, dstCol):
	if dstRow > 19:
		return False
	if dstCol > 19:
		return False
	if grid[srcRow][srcCol]+20 == grid[dstRow][dstCol]:
		return True
	if grid[srcRow][srcCol]+1 == grid[dstRow][dstCol]:
		return True
	return False
	

if __name__ == "__main__":
	Problem15()
