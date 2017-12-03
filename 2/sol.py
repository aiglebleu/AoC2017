#!/usr/bin/env python3

x = []

for line in open('input'):
	arr = [ int(s) for s in line.split() ]
	x.append(max(arr) - min(arr))

print(sum(x))
