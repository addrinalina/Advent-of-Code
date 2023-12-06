# https://adventofcode.com/2023/day/5

import re

with open("C:\\Users\\aromo\\OneDrive - No Hunger Forum\\Documentos\\Advent of Code\\input5.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
# print(x)

seedtosoil = []
soiltofert = []
fertowat = []
watolight = []
lightotemp = []
temptohum = []
humtoloc = []

i = 0
line = x[i]
# En "seeds" estan todas las semillas, empezamos el mapeo
if len(re.findall("seeds",line)) != 0:
    seeds = re.findall(r"\d+", line)
    i+=1
    line = x[i]
print(seeds)
while len(re.findall("soil-to-fertilizer", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    print(num)
    if len(num) != 0:
        seedtosoil.append(num)
    i+=1
    line = x[i]
print(seedtosoil)
while len(re.findall("fertilizer-to-water", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    if len(num) != 0:
        soiltofert.append(num)
    i+=1
    line = x[i]
print(soiltofert)
while len(re.findall("water-to-light", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    if len(num) != 0:
        fertowat.append(num)
    i+=1
    line = x[i]
print(fertowat)
while len(re.findall("light-to-temperature", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    if len(num) != 0:
        watolight.append(num)
    i+=1
    line = x[i]
print(watolight)
while len(re.findall("temperature-to-humidity", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    if len(num) != 0:
        lightotemp.append(num)
    i+=1
    line = x[i]
print(lightotemp)
while len(re.findall("humidity-to-location", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    if len(num) != 0:
        temptohum.append(num)
    i+=1
    line = x[i]
print(temptohum)
while i < len(x):
    line = x[i]
    num = [int(n) for n in re.findall(r"\d+", line)]
    if len(num) != 0:
        humtoloc.append(num)
    i+=1
print(humtoloc)
print("mapeo hecho")

soils = []
ferts = []
wats = []
lights = []
temps = []
hums = []
locs = []

seedpairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2) if i + 1 < len(seeds)]

for i, pair in enumerate(seedpairs):
    for seed in range(int(pair[0]),int(pair[0])+int(pair[1])):
        for tuple in seedtosoil:
            if tuple[1] <= seed < tuple[1]+tuple[2]:
                soils.append(tuple[0]+(seed-tuple[1])) 
        if len(soils) == i:
            soils.append(seed)
print("Tengo soils")

for i, soil in enumerate(soils):
    soil = int(soil)
    for tuple in soiltofert:
        if tuple[1] <= soil < tuple[1]+tuple[2]:
            ferts.append(tuple[0]+(soil-tuple[1])) 
    if len(ferts) == i:
        ferts.append(soil)
print("Tengo ferts")

for i, fert in enumerate(ferts):
    fert = int(fert)
    for tuple in fertowat:
        if tuple[1] <= fert < tuple[1]+tuple[2]:
            wats.append(tuple[0]+(fert-tuple[1])) 
    if len(wats) == i:
        wats.append(fert)
print("Tengo wats")

for i, wat in enumerate(wats):
    wat = int(wat)
    for tuple in watolight:
        if tuple[1] <= wat < tuple[1]+tuple[2]:
            lights.append(tuple[0]+(wat-tuple[1])) 
    if len(lights) == i:
        lights.append(wat)
print("Tengo lights")

for i, light in enumerate(lights):
    light = int(light)
    for tuple in lightotemp:
        if tuple[1] <= light < tuple[1]+tuple[2]:
            temps.append(tuple[0]+(light-tuple[1])) 
    if len(temps) == i:
        temps.append(light)
print("Tengo temps")

for i, temp in enumerate(temps):
    temp = int(temp)
    for tuple in temptohum:
        if tuple[1] <= temp < tuple[1]+tuple[2]:
            hums.append(tuple[0]+(temp-tuple[1])) 
    if len(hums) == i:
        hums.append(temp)
print("Tengo hums")

for i, hum in enumerate(hums):
    hum = int(hum)
    for tuple in humtoloc:
        if tuple[1] <= hum < tuple[1]+tuple[2]:
            locs.append(tuple[0]+(hum-tuple[1])) 
    if len(locs) == i:
        locs.append(hum)
print("Tengo locs")

print("Final locs", locs)
print(min(locs))


