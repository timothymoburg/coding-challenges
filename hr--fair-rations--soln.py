#!/bin/python3


def soln(b):
	odds = []
	for i in range(len(b)):
		if (b[i]%2 != 0):
			odds.append(i)
	if (len(odds)%2 != 0):
		return "NO"
	swaps = 0
	for i in range(1,len(odds),2):
		swaps += odds[i] - odds[i-1]
	return 2*swaps


n = int(input().strip())
b = [int(i) for i in input().strip().split(' ')]
print(soln(b))
