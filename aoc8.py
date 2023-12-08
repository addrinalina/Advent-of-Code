# https://adventofcode.com/2023/day/8

import ast

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-23\\input8.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

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
loc = 'AAA'

while loc != 'ZZZ':
    j = i
    if j >= len(rightleft):
        j = j%len(rightleft)
    newloc = nodes[loc][rightleft[j]]
    loc = newloc
    i += 1
    print(loc)

print("Total steps", i)
