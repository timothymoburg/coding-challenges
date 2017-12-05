#!/bin/python3

def find_princess(n,grid):
	for y in range(n):
		for x in range(n):
			if (grid[y][x] == 'p'):
				return (x,y)

def y_direction(p,r,alt):
	if (p < r):
		return "UP"
	elif (p > r):
		return "DOWN"
	else:
		return alt

def next_move(n,grid,r_x,r_y):
	p_x,p_y = find_princess(n,grid)

	if (p_x < r_x):
		res = y_direction(p_y,r_y,"LEFT")
	elif (p_x > r_x):
		res = y_direction(p_y,r_y,"RIGHT")
	else:
		res = y_direction(p_y,r_y,"FOUND")
	return res

n = int(input().strip())
y,x = [int(i) for i in input().strip().split(' ')]
grid = [] 
for i in range(n):
	grid.append(input().strip())
print(next_move(n,grid,x,y))
