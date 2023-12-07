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
    order =  {'J':0, '2':1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}
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
    js = 0
    if 'J' in count and count['J'] != 5:
        js += count['J']
        del count['J']
    count = sorted(list(count.values()))
    count[-1] += js
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