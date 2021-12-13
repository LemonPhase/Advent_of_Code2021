import os
from collections import defaultdict
dirpath = os.path.dirname(os.path.realpath(__file__))
os.chdir(dirpath)


f = open("day5_input.txt", 'r')
d_part1 = defaultdict(int)
d_part2 = defaultdict(int)
for line in f.read().splitlines():
    start, end = line.split(" -> ")
    # Starting coord
    x1, y1 = start.split(",")
    # End coord
    x2, y2 = end.split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    # Distance moved in x and y direction
    x_d, y_d = x2 - x1, y2 - y1

    for i in range(1 + max(abs(x_d), abs(y_d))):
        x = x1 + (1 if x_d > 0 else (-1 if x_d < 0 else 0)) * i
        y = y1 + (1 if y_d > 0 else (-1 if y_d < 0 else 0)) * i
        d_part1[(x, y)] += 1 if x_d == 0 or y_d == 0 else 0
        d_part2[(x, y)] += 1

print(len([i for i in d_part1 if d_part1[i] > 1]))
print(len([i for i in d_part2 if d_part2[i] > 1]))


f.close()
