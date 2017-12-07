#!/usr/bin/env python3

lines = []

for line in open('input'):
    line = line.strip()
    lines.append(int(line))

index = lines[0]
count = 0

#print(lines)

while index >= 0 and index < len(lines):
    #print("{} => {}".format(count, index))
    offset = lines[index]
    lines[index] += 1
    index += offset
    #print("jumping to {} (offset {})".format(index, offset))
    count += 1

print(count)

