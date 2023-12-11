# https://adventofcode.com/2023/day/11

import re
import numpy as np
import copy

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-23\\input11.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]


x = [list(row) for row in x]
# expanded = x.copy()

emptyrows = []
emptycols = []

# j = 0
for i in range(len(x)):
    if all(char == '.' for char in x[i]):
        emptyrows.append(i)

print(emptyrows)

transposed = np.transpose(x)
# transexp = list(transposed.copy())

# j = 0
for i in range(len(transposed)):
    if all(char == '.' for char in transposed[i]):
        emptycols.append(i)
    
# finalexp = np.transpose(transexp)
print(emptycols)

exp = 999999

original_coords = []
for i in range(len(x)):
    for j in range(len(x[0])):
        if x[i][j] == '#':
            original_coords.append([i,j])

print(original_coords)
dists = []
final_coords = copy.deepcopy(original_coords)

# First rows, coordenada left
for row in emptyrows:
    for i in range(len(original_coords)):
        # print(original_coords[i])
        if original_coords[i][0] > row:
            final_coords[i][0] += exp
            # print("Añado", exp, "a la fila", original_coords[i][0], "y se va a", final_coords[i])
# Now cols
for col in emptycols:
    for i in range(len(original_coords)):
        if original_coords[i][1] > col:
            # print("Añado", exp, "a la columna", coord[1])
            final_coords[i][1] += exp

print(original_coords)
print(final_coords)

for i in range(len(final_coords)):
    for j in range(i+1,len(final_coords)):
        dist = abs(final_coords[j][0]-final_coords[i][0]) + abs(final_coords[j][1]-final_coords[i][1])
        # print("Entre", i+1, "y", j+1, "hay", dist)
        dists.append(dist)

print(dists)
print(sum(dists))


