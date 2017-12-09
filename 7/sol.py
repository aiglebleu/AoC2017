#!/usr/bin/env python3

parents = set()
children = set()
parenthood = set()
weights = {}

def children_of(node):
    return set([child for parent, child in parenthood if parent == node])

memo = {}
def weight(node):
    total = weights[node]
    for child in children_of(node):
        if child not in memo:
            memo[child] = weight(child)
        total += memo[child]
    return total

def find_balanced(node):
    w = list(map(weight, children_of(node)))
    s = set(w)
    print(w, s)
    if len(s) == 1:
        return node
    val = s.pop()
    return val if w.count(val) == 1 else s.pop()

for line in open('input'):
    arr = line.split()
    parents.add(arr[0])
    weights[arr[0]] = int(arr[1][1:-1])
    if '->' in line:
        for child in arr[arr.index('->')+1:]:
            children.add(child.strip(","))
            parenthood.add( (arr[0], child.strip(",")) )

print("Bottom is {}".format(parents - children))
print(children_of("bpvhwhh"))
print(weights["bpvhwhh"])
print(weight("bpvhwhh"))
balanced("bpvhwhh")
