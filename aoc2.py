with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code\\input2.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

res = []

for i, game in enumerate(x):
    print(i, game)
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
        if char == "b":
            if int(num) > 14:
                pos = False
                print("Muchos blues")
                break
            num = "0"        
        elif char == "g":
            if int(num) > 13:
                pos = False
                print("Muchos green")
                break
            num = "0"   
        elif char == "r":
            if int(num) > 12:
                pos = False
                print("Muchos red")
                break
            num = "0"   

    if pos:
        print("Este sí")
        res.append(i+1)

print(res)
print(sum(res))
