# https://adventofcode.com/2023/day/6

from collections import Counter
import re

with open("C:\\Users\\aromo\\OneDrive - No Hunger Forum\\Documentos\\Advent of Code\\input7.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)


hands = []
bids = {}

def custom_sort_key1(s):
    order =  {'2':0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    return [order.get(c, float('inf')) for c in s]

def custom_sort_key2(key):
    order = {None: 0, (1,1,1,1,1): 1, (1,1,1,2): 2, (1,2,2): 3, (1,1,3): 4, (2,3): 5, (1,4): 6, (5,): 7}
    return order.get(key, float('inf'))

for line in x:
    hand, bid = line.strip().split(' ')
    hands.append(hand)
    bids[hand] = int(bid)

print(hands)
print(bids)

counts = {}
ranks = {}

for hand in hands:
    count = Counter(hand)
    count = sorted(list(count.values()))
    counts[hand] = count

grouped_hands = {}

for hand, count in counts.items():
    count_tuple = tuple(count)
    if count_tuple not in grouped_hands:
        grouped_hands[count_tuple] = [hand]
    else:
        grouped_hands[count_tuple].append(hand) 

grouped_hands = sorted(grouped_hands.items(), key = lambda x: custom_sort_key2(x[0]))

grouped_hands = dict(grouped_hands)

k = 1
for tuple, hand in grouped_hands.items():
    if len(hand) == 1:
        ranks[hand[0]] = k
        k += 1
    else:
        sorted_hand = sorted(hand, key=custom_sort_key1)
        for j, word in enumerate(sorted_hand):
            ranks[word] = j+k
        k += len(sorted_hand)
print(ranks)

results = {}

for hand in hands:
    results[hand] = bids[hand]*ranks[hand]

print(results)

print(sum(results.values()))

