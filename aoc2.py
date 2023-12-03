with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code\\input2.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

mincubes = {"b":0, "g":0, "r":0}
res = []

for i, game in enumerate(x):
    pos = True
    dentro = False
    num = "0"
    j = 0
    while j < len(game):
        char = game[j]
        k = 0
        if char == ":":
            dentro = True
        while dentro & char.isdigit():
            num = num+char
            k += 1
            char = game[j+k]
        j += k+1
        if (char in ["b", "g", "r"]):
            if (int(num) > mincubes[char]):
                mincubes[char] = int(num)
            num = "0"
    print("Game ", i, mincubes)

    # Calculation of the power of the set
    power = 1
    for value in mincubes.values():
        power *= value
    print(power)
    res.append(power)
    mincubes = {"b":0, "g":0, "r":0}
    
print(res)
print(sum(res))
