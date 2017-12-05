#!/bin/python3

def display_path_to_princess(n,grid):
	if (grid[0][0] == 'p'):
		x = "LEFT"
		y = "UP"
	elif (grid[0][-1] == 'p'):
		x = "RIGHT"
		y = "UP"
	elif (grid[n-1][0] == 'p'):
		x = "LEFT"
		y = "DOWN"
	elif (grid[n-1][n-1] == 'p'):
		x = "RIGHT"
		y = "DOWN"
	else:
		return 0
	for i in range(n//2):
		print(x,y,sep="\n")
	return 1

n = int(input().strip())
grid = [] 
for i in range(n):
	grid.append(input().strip())

display_path_to_princess(n,grid)
