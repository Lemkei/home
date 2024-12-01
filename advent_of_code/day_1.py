"""
https://adventofcode.com/2024/day/1

rawddoging it, so only standard library, no AI

"""

with open('day_1_input.txt') as ds:
    d1_input = ds.read()

raw_list = d1_input.split()

l1 = []
l2 = []

for i in range(len(raw_list)):
    if len(l1) == len(l2):
        l1.append(raw_list[i])
    else:
        l2.append(raw_list[i])

l1.sort()
l2.sort()

lf = [l1, l2]

distance = 0

for i in range(len(lf[0])):
    distance += abs(int(lf[0][i]) - int(lf[1][i]))

print(distance)

