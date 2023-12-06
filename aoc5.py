# https://adventofcode.com/2023/day/5

import re

with open("C:\\Users\\aromo\\OneDrive - No Hunger Forum\\Documentos\\Advent of Code\\input5.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water ={}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

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
        for j in range(num[2]):
            seed_to_soil[num[1]+j] = num[0]+j
    i+=1
    line = x[i]
print(seed_to_soil)
while len(re.findall("fertilizer-to-water", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    print(num)
    if len(num) != 0:
        for j in range(num[2]):
            soil_to_fertilizer[num[1]+j] = num[0]+j
    i+=1
    line = x[i]
print(soil_to_fertilizer)
while len(re.findall("water-to-light", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    print(num)
    if len(num) != 0:
        for j in range(num[2]):
            fertilizer_to_water[num[1]+j] = num[0]+j
    i+=1
    line = x[i]
print(fertilizer_to_water)
while len(re.findall("light-to-temperature", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    print(num)
    if len(num) != 0:
        for j in range(num[2]):
            water_to_light[num[1]+j] = num[0]+j
    i+=1
    line = x[i]
print(water_to_light)
while len(re.findall("temperature-to-humidity", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    print(num)
    if len(num) != 0:
        for j in range(num[2]):
            light_to_temperature[num[1]+j] = num[0]+j
    i+=1
    line = x[i]
print(light_to_temperature)
while len(re.findall("humidity-to-location", line)) == 0:
    num = [int(n) for n in re.findall(r"\d+", line)]
    print(num)
    if len(num) != 0:
        for j in range(num[2]):
            temperature_to_humidity[num[1]+j] = num[0]+j
    i+=1
    line = x[i]
print(temperature_to_humidity)
while i < len(x):
    line = x[i]
    num = [int(n) for n in re.findall(r"\d+", line)]
    print(num)
    if len(num) != 0:
        for j in range(num[2]):
            humidity_to_location[num[1]+j] = num[0]+j
    i+=1
print(humidity_to_location)

result = []

for seed in seeds:
    seed = int(seed)
    if seed in seed_to_soil.keys():
        soil = seed_to_soil[seed]
    else:
        soil = seed
    if soil in soil_to_fertilizer.keys():
        fert = soil_to_fertilizer[soil]
    else:
        fert = soil
    if fert in fertilizer_to_water.keys():
        water = fertilizer_to_water[fert]
    else:
        water = fert
    if water in water_to_light.keys():
        light = water_to_light[water]
    else:
        light = water
    if light in light_to_temperature.keys():
        temp = light_to_temperature[light]
    else:
        temp = light
    if temp in temperature_to_humidity.keys():
        hum = temperature_to_humidity[temp]
    else:
        hum = temp
    if hum in humidity_to_location.keys():
        loc = humidity_to_location[hum]
    else:
        loc = hum
    result.append(loc)
print(result)
print(min(result))


