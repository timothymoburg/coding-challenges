#!/bin/python3

def find_closest(grid,r_x,r_y):
	locs = []
	for y in range(5):
		for x in range(5):
			if (grid[y][x] == 'd'):
				locs.append((x,y))
	min_loc = (0,0)
	min_dist = 10
	for loc in locs:
		dist = 0
		dist += abs(r_y-loc[1])
		dist += abs(r_x-loc[0])
		if (dist < min_dist):
			min_loc = loc
			min_dist = dist
	return min_loc


def y_direction(p,r,alt):
	if (p < r):
		return "UP"
	elif (p > r):
		return "DOWN"
	else:
		return alt

def next_move(grid,r_x,r_y):
	p_x,p_y = find_closest(grid,r_x,r_y)

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
