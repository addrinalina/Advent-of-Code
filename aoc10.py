# https://adventofcode.com/2023/day/10

import numpy as np

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-23\\input10.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

pos_dict = {}

def nextS(matrix, row, col):
    coords = [0,0]
    found = False
    if col - 1 >= 0:
        if matrix[row][col - 1] in ['-','L','F'] and found == False:
            coords = [row, col-1]
            found = True
            if matrix[row][col - 1] == '-':
                # left = [0,-1]
                next = "left"
            elif matrix[row][col - 1] == 'L':
                # up = [-1,0]
                next = "up"
            elif matrix[row][col - 1] == 'F':
                # down = [1,0]
                next = "down"
            print("Coords", coords, "tienen un 1 porque hay una ", matrix[row][col - 1], "y voy a", next)

    if col + 1 < len(matrix[0]):
        if matrix[row][col + 1] in ['-','7','J'] and found == False:
            coords = [row, col+1]
            found = True
            if matrix[row][col + 1] == '-':
                next = "right"
            elif matrix[row][col + 1] == '7':
                next = "down"
            elif matrix[row][col + 1] == 'J':
                next = "up"
            print("Coords", row, col+1, "tienen un 1 porque hay una ", matrix[row][col + 1], "y voy a ", next)

    if row - 1 >= 0:
        if matrix[row - 1][col] in ['|','7','F'] and found == False:
            coords = [row-1, col]
            found = True
            if matrix[row - 1][col] == '|':
                next = "up"
            elif matrix[row - 1][col] == '7':
                next = "left"
            elif matrix[row - 1][col] == 'F':
                next = "right"
            print("Coords", row-1, col, "tienen un 1 porque hay una ", matrix[row-1][col], "y voy a ", next)

    if row + 1 < len(matrix):
        if matrix[row + 1][col] in ['|','L','J'] and found == False:
            coords = [row+1, col]
            found = True
            if matrix[row + 1][col] == '|':
                next = "down"
            elif matrix[row + 1][col] == 'L':
                next = "right"
            elif matrix[row + 1][col] == 'J':
                next = "left"            
            print("Coords", row+1, col, "tienen un 1 porque hay una ", matrix[row+1][col], "y voy a ", next)
    print(coords, next)
    return coords, next

def nextnode(matrix, row, col, step):
    loc = [row, col]

    if step == "right":
        loc[1] += 1
        # print("Voy a ", loc, "que hay", matrix[loc[0]][loc[1]])
        if matrix[loc[0]][loc[1]] == '-':
            next = "right"
        elif matrix[loc[0]][loc[1]] == '7':
            next = "down"
        elif matrix[loc[0]][loc[1]] == 'J':
            next = "up"
        else: 
            next = "S"
    elif step == "left":
        # print("vengo de la der")
        loc[1] -= 1
        if matrix[loc[0]][loc[1]] == '-':
            next = "left"
        elif matrix[loc[0]][loc[1]] == 'L':
            next = "up"
        elif matrix[loc[0]][loc[1]] == 'F':
            next = "down"
        else: 
            next = "S"
    elif step == "up":
        # print("vengo de abajo")
        loc[0] -= 1
        if matrix[loc[0]][loc[1]] == '|':
            next = "up"
        elif matrix[loc[0]][loc[1]] == '7':
            next = "left"
        elif matrix[loc[0]][loc[1]] == 'F':
            next = "right"
        else: 
            next = "S"
    elif step == "down":
        # print("vengo de arriba")
        loc[0] += 1
        if matrix[loc[0]][loc[1]] == '|':
            next = "down"
        elif matrix[loc[0]][loc[1]] == 'L':
            next = "right"
        elif matrix[loc[0]][loc[1]] == 'J':
            next = "left"         
        else: 
            next = "S"
    return loc, next


rows = len(x)
columns = len(x[0])

loc = [0,0]
start = False
history = []

for i in range(rows):
    for j in range(columns):
        if x[i][j] == 'S':
            start = True
            loc, next = nextS(x, i, j)
            print("He encontrado la S, estoy en", loc, " y voy hacia", next)
            # history.append([i,j])

while next != 'S':
    history.append(loc)
    print("ahora estoy en ", loc, "y hay ", x[loc[0]][loc[1]], "y voy a ", next)
    loc, next = nextnode(x, loc[0], loc[1], next)
    
print(history)
lejos = int(len(history)/2)
print("El mas lejano es ", history[lejos], "que está a", lejos+1)
    


