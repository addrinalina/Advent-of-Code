# https://adventofcode.com/2023/day/11

import re
import numpy as np

with open("C:\\Users\\aromo\\OneDrive - No Hunger Forum\\Documentos\\Advent of Code\\input11.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]


x = [list(row) for row in x]
expanded = x.copy()


j = 0
for i in range(len(x)):
    if all(char == '.' for char in x[i]):
        expanded.insert(i+j, x[i].copy())
        j += 1


transposed = np.transpose(expanded)
transexp = list(transposed.copy())

j = 0
for i in range(len(transposed)):
    if all(char == '.' for char in transposed[i]):
        transexp.insert(i+j, transposed[i].copy())
        j += 1
    
finalexp = np.transpose(transexp)

for line in finalexp:
    print(line)

coords = []
for i in range(len(finalexp)):
    for j in range(len(finalexp[0])):
        if finalexp[i][j] == '#':
            coords.append([i,j])

print(coords)
dists = []

for i in range(len(coords)):
    for j in range(i+1,len(coords)):
        dist = abs(coords[j][0]-coords[i][0]) + abs(coords[j][1]-coords[i][1])
        # print("Entre", i+1, "y", j+1, "hay", dist)
        dists.append(dist)

print(dists)
print(sum(dists))


