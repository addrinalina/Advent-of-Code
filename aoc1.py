with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code\\input1.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

result = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = [1,2,3,4,5,6,7,8,9]
lista = []

for line in x:
    print(line)
    found = False
    for i, char in enumerate(line):
        if char.isdigit():
            first = char
            break
        for k in range(len(digits)):
            if char == digits[k][0]:
                j = 1
                while line[i+j] == digits[k][j]:
                    if j == len(digits[k])-1:
                        first = numbers[k]
                        found = True
                        break
                    j += 1
            if found:
                break
        if found:
            break
    print("FIRST", first)

    found = False
    for i, char in enumerate(line[::-1]):
        if char.isdigit():
            last = char
            break
        for k in range(len(digits)):
            if char == digits[k][-1]:
                j = 1
                while line[::-1][i+j] == digits[k][::-1][j]:
                    if j == len(digits[k])-1:
                        last = numbers[k]
                        found = True
                        break
                    j += 1
            if found:
                break
        if found:
            break
    print("LAST", last)

    num = int(first)*10 + int(last)
    print(num)

    lista.append(num)

    result += num

print(lista)

print("RESULTADO = ", result)

