#!/bin/python3


def find_d(grid):
	locs = []
	for y in range(5):
		for x in range(5):
			if (grid[y][x] == 'd'):
				return (x,y)

def y_direction(p,r,alt):
	if (p < r):
		return "UP"
	elif (p > r):
		return "DOWN"
	else:
		return alt

def next_move(grid,r_x,r_y):
	p_x,p_y = find_d(grid)

	if (p_x < r_x):
		res = y_direction(p_y,r_y,"LEFT")
	elif (p_x > r_x):
		res = y_direction(p_y,r_y,"RIGHT")
	else:
		res = y_direction(p_y,r_y,"CLEAN")
	return res

y,x = [int(i) for i in input().strip().split(' ')]
grid = [] 
for i in range(5):
	grid.append(input().strip())
print(next_move(grid,x,y))
