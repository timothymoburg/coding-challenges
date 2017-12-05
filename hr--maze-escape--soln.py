#!/bin/python3

def next_loc(pos,deg,stack,nonstack,m):
	deg_names = {0:"UP", 90:"LEFT", 180:"DOWN", 270:"RIGHT"}
	posz = {0:(pos[0],pos[1]+1),1:(pos[0]-1,pos[1]),2:(pos[0],pos[1]-1),3:(pos[0]+1,pos[1])}
	visited = set(stack+nonstack)
	dirs = [m[0][1],m[1][0],m[2][1],m[1][2]]*2
	b = 4 - deg//90
	cells_0 = dirs[b:b+4]
	backtrack = True
	deg_0 = 0
	four = [2,1,3,0]
	for i in four:
		if (cells_0[i] == "e"):
			deg_0 = i
			backtrack = False
			break
		elif (cells_0[i] == "-" and posz[i] not in visited):
			deg_0 = i
			backtrack = False
	if (backtrack):
		nonstack.append(stack.pop())
		new_pos = stack[-1]
		if (new_pos[1] > pos[1]):
			deg_0 = 0
		elif (new_pos[0] < pos[0]):
			deg_0 = 1
		elif (new_pos[1] < pos[1]):
			deg_0 = 2
		elif (new_pos[0] > pos[0]):
			deg_0 = 3
		else:
			raise ValueError
	else:
		new_pos = posz[deg_0]
		stack.append(new_pos)
	new_deg_M = (360 - deg + 90*deg_0)%360
	new_deg_0 = (deg + new_deg_M)%360
	print(deg_names[new_deg_M])
	return (new_pos, new_deg_0, stack, nonstack)


def main(pID,maze):
	breaky = False
	for m in range(3):
		if (breaky):
			break
		for n in range(3):
			if (maze[m][n] == "e"):
				if (m > 0 and maze[m-1][n]=="-"):
					maze[m-1][n] = "e"
				if (m < 2 and maze[m+1][n]=="-"):
					maze[m+1][n] = "e"
				if (n > 0 and maze[m][n-1]=="-"):
					maze[m][n-1] = "e"
				if (n < 2 and maze[m][n+1]=="-"):
					maze[m][n+1] = "e"
				breaky = True
				break
	try:
		f = open("botinfo{}".format(pID),"r+")
	except FileNotFoundError:
		f = open("botinfo{}".format(pID),"w")
		position = (1,-1)
		degrees = 0
		stack = [(1,-1)]
		nonstack = []
	else:
		f_info = f.readlines()
		position = eval(f_info[0])
		degrees = int(f_info[1])
		stack = eval(f_info[2])
		nonstack = eval(f_info[3])
	finally:
		f.seek(0,0)
		pos,deg,stack,nonstack = next_loc(position,degrees,stack,nonstack,maze)
		f.write("{}\n".format(str(pos)))
		f.write("{}\n".format(str(deg)))
		f.write("{}\n".format(str(stack)))
		f.write("{}\n".format(str(nonstack)))
		f.close()

pID = str(input().strip())
maze = []
for i in range(3):
	maze.append(list(input().strip()))
main(pID,maze)
