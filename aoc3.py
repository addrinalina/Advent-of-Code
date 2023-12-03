# https://adventofcode.com/2023/day/3 - Assuming that no gear is adjacent to 3 numbers, and that each number can only be adjacent to one "*"

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code\\input3.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
# print(x)

def is_symbol(char):
    return char.isascii() and not char.isalnum() and char != '.'

def adjacent_symbol(matrix, row, col):
    result = False
    if col - 1 >= 0:
        if is_symbol(matrix[row][col - 1]):
            result = True

    if col + 1 < len(matrix[0]):
        if is_symbol(matrix[row][col + 1]):
            result = True

    if row - 1 >= 0:
        if is_symbol(matrix[row - 1][col]):
            result = True

    if row + 1 < len(matrix):
        if is_symbol(matrix[row + 1][col]):
            result = True

    if row - 1 >= 0 and col - 1 >= 0:
        if is_symbol(matrix[row - 1][col - 1]):
            result = True

    if row - 1 >= 0 and col + 1 < len(matrix[0]):
        if is_symbol(matrix[row - 1][col + 1]):
            result = True

    if row + 1 < len(matrix) and col - 1 >= 0:
        if is_symbol(matrix[row + 1][col - 1]):
            result = True

    if row + 1 < len(matrix) and col + 1 < len(matrix[0]):
        if is_symbol(matrix[row + 1][col + 1]):
            result = True

    return result

def adjacent_gear(matrix, row, col):
    result = False
    coords = []
    if col - 1 >= 0:
        if matrix[row][col - 1] == "*":
            result = True
            coords = [row,col-1]

    if col + 1 < len(matrix[0]):
        if matrix[row][col + 1] == "*":
            result = True
            coords = [row, col+1]

    if row - 1 >= 0:
        if matrix[row - 1][col] == "*":
            result = True
            coords = [row-1, col]

    if row + 1 < len(matrix):
        if matrix[row + 1][col] == "*":
            result = True
            coords = [row+1, col]

    if row - 1 >= 0 and col - 1 >= 0:
        if matrix[row - 1][col - 1] == "*":
            result = True
            coords = [row-1, col-1]

    if row - 1 >= 0 and col + 1 < len(matrix[0]):
        if matrix[row - 1][col + 1] == "*":
            result = True
            coords = [row-1, col+1]

    if row + 1 < len(matrix) and col - 1 >= 0:
        if matrix[row + 1][col - 1] == "*":
            result = True
            coords = [row+1, col-1]

    if row + 1 < len(matrix) and col + 1 < len(matrix[0]):
        if matrix[row + 1][col + 1] == "*":
            result = True
            coords = [row+1, col+1]

    return result, coords

rows = len(x)
columns = len(x[0])
num = ""
partnumber = False
gearnumber = False
partlist = []
gearlist = []
gearratios = []
for i in range(rows):
    for j in range(columns):
        if not x[i][j].isdigit():
            if partnumber:
                partlist.append(int(num))
            partnumber = False
            if gearnumber:
                gearlist.append([int(num), gearcoords])
            gearnumber = False
            num = ""
        else:
            if adjacent_symbol(x, i, j):
                partnumber = True
            num += x[i][j]
            if adjacent_gear(x,i,j)[0]:
                gearnumber = True
                gearcoords = adjacent_gear(x,i,j)[1]
print("List of part numbers", partlist)
print("Sum of part numbers", sum(partlist))

print("List of gear numbers", gearlist)

for i, number in enumerate(gearlist):
    for j in range(i+1, len(gearlist)):
        if number[1] == gearlist[j][1]:
            print("Gear pair", number[0], gearlist[j][0])
            gearratios.append(number[0]*gearlist[j][0])

print("List of gear ratios", gearratios)
print("Sum of gear ratios", sum(gearratios))