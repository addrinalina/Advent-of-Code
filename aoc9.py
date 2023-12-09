# https://adventofcode.com/2023/day/9

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-23\\input9.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
# print(x)

adds = []
subs = []

for line in x:
    values = line.split(' ')
    values = [int(value) for value in values]
    history = [values[:]]
    difs = values[:]
    # print(values)
    while not all(dif == 0 for dif in difs):
        i = 0
        while i < (len(difs)-1):
            difs[i] = difs[i+1]-difs[i]
            i += 1
        difs = difs[:-1]
        history.append(difs.copy())

    history.reverse()
    # print(history)

    i = 0
    while i < len(history):
        if i == 0:
            history[i].append(0)
            history[i].insert(0, 0)
        else:
            history[i].append(history[i-1][-1]+history[i][-1])
            history[i].insert(0, history[i][0]-history[i-1][0])
        i += 1
    adds.append(history[-1][-1])
    subs.append(history[-1][0])
print(adds)
print(subs)

print(sum(adds))
print(sum(subs))
        