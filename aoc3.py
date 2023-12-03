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

rows = len(x)
columns = len(x[0])
num = ""
partnumber = False
partlist = []
for i in range(rows):
    for j in range(columns):
        if not x[i][j].isdigit():
            if partnumber:
                partlist.append(int(num))
            num = ""
            partnumber = False
        else:
            if adjacent_symbol(x, i, j):
                partnumber = True
            num += x[i][j]
print(partlist)
print(sum(partlist))