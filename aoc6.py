# https://adventofcode.com/2023/day/6

import re

with open("C:\\Users\\aromo\\OneDrive - No Hunger Forum\\Documentos\\Advent of Code\\input6.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

times = re.findall(r"\d+", x[0])
times = [int(time) for time in times]
distances = re.findall(r"\d+", x[1])
distances = [int(dist) for dist in distances]

print(times)
print(distances)

ways = [0]*len(times)

# i es cada carrera
for i in range(len(times)):
    for segs in range(times[i]):
        dist = (times[i] - segs)*segs
        if dist > distances[i]:
            ways[i] += 1
print(ways)

result = 1
for value in ways:
    result *= value
print(result)