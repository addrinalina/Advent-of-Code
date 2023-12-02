with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code\\input1.txt") as f:
    x = [line[:-1] for line in f.readlines()]
print(x)

result = 0

for line in x:

    for char in line:
        if char.isdigit():
            last = char

    for char in line[::-1]:
        if char.isdigit():
            first = char

    num = int(first)*10 + int(last)

    print(num)

    result += num

print(result)

