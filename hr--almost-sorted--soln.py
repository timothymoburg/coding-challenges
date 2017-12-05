#!/bin/python3


def test_changes(d,err,method):
	a = err[0]
	b = err[-1]
	a_0 = d[b+1] if a==0 else d[a-1]
	a_1 = d[a]
	a_2 = d[a+1]
	b_0 = d[b]
	b_1 = d[b+1]
	b_2 = d[a] if b==len(d)-2 else d[b+2]
	if (a_0<=b_1 and b_1<=a_2 and b_0<=a_1 and a_1<=b_2):
		print("yes\n{0} {1} {2}".format(method,a+1,b+2))
		return 1
	else:
		print("no")
		return 0

def soln(d):
	err = []
	last = d[0]
	for i in range(1,len(d)):
		curr = d[i]
		if (curr < last):
			err.append(i-1)
		last = curr
	if (len(err) == 0):
		print("yes")
		return 1
	elif (len(err) == 1):
		err.append(err[0])
		ans = test_changes(d,err,"swap")
		return ans
	elif (len(err) == 2):
		ans = test_changes(d,err,"swap")
		return ans
	else:
		last = err[0]
		for i in range(1,len(err)):
			if (err[i] != last+1):
				print("no")
				return 0
			last +=1
		ans = test_changes(d,err,"reverse")
		return ans

n = int(input().strip())
d = [int(i) for i in input().strip().split(' ')]
soln(d)
