#!/usr/bin/env python3

total = 0

for line in open('input'):
    arr = line.split()
    if sorted(arr) == sorted(list(set(arr))):
        total += 1

print(total)
