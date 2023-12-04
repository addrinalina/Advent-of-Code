# https://adventofcode.com/2023/day/4

with open("C:\\Users\\aromo\\OneDrive - No Hunger Forum\\Documentos\\Advent of Code\\input4.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]

points = []

for i, game in enumerate(x):
    dentro = False
    propios = False
    num = ""    
    j = 0
    winning = []
    own = []
    calculo = 0
    while j < len(game):
        char = game[j]
        k = 0
        if char == ":":
            dentro = True
        if char == "|":
            propios = True
        while dentro & char.isdigit():
            num = num+char
            k += 1
            if (j+k) == len(game):
                break
            char = game[j+k]
        if (not propios) and num != "":
            winning.append(int(num))
            num = ""
        if propios and num != "":
            if int(num) in winning:
                calculo += 1
            num = ""
        j += k+1
    # print("Los winning numbers del game", i, "son", winning)
    points.append(calculo)
    # print("El game", i+1, "tiene", calculo, "puntos")

print("Los juegos ganan estos puntos:",points)
print("La suma de los puntos es: ", sum(points))

copies = [1 for _ in range(len(x))]

for i in range(len(points)):
    cards = copies[i]
    while cards > 0:
        j = i+1
        number = points[i]
        while number > 0:
            copies[j] += 1
            number -= 1
            j += 1
        cards -= 1
print("Copias: ",copies)
print("La suma de las copias es", sum(copies))