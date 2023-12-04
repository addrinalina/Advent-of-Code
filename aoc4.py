with open("C:\\Users\\aromo\\OneDrive - No Hunger Forum\\Documentos\\Advent of Code\\input4.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

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
                # print("El numero", num, "es ganador del juego", i+1)
                if calculo == 0:
                    calculo = 1
                else:
                    calculo *= 2
            num = ""
        j += k+1
    # print("Los winning numbers del game", i, "son", winning)
    points.append(calculo)
    # print("El game", i+1, "tiene", calculo, "puntos")

print("Los juegos ganan estos puntos:",points)
print("La suma de los puntos es: ", sum(points))