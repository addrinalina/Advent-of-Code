# https://adventofcode.com/2023/day/8

import ast
import math
from functools import reduce

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-23\\input8.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

nodes = {}
rightleft = []

for i, line in enumerate(x):
    if i == 0 or i == 1:
        for char in line:
            if char == 'L':
                rightleft.append(0)
            elif char == 'R':
                rightleft.append(1)

    else:
        parts = line.split('=')
        key = parts[0].strip()
        print(parts)
        value = tuple(map(str.strip, parts[1][2:-1].split(',')))
        print(value)
        nodes[key]= value
print(rightleft)
print(nodes)

i = 0

print(nodes.keys())

loc = [node for node in nodes.keys() if node.endswith('A')]

print(loc)
cicles = [0]*len(loc)

while 0 in cicles:
    j = i
    if j >= len(rightleft):
        j = j%len(rightleft)
    for k, node in enumerate(loc):
        newloc = nodes[node][rightleft[j]]
        loc[k] = newloc
        if newloc.endswith('Z') and cicles[k] == 0:
            cicles[k] = i+1
    i += 1    

print(cicles)

mcm = reduce(lcm, cicles)

print("Steps = ", mcm)
