import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

f = open("day4_input.txt", 'r')
init = f.read().splitlines()
f.close()

# First line, numbers for bingo
n_list = [int(i) for i in init.pop(0).split(',')]
grids = []

# 2D list for the grids
for line in init:
    grids.append([int(i) for i in line.split()])

# print(n_list)
# print(grids)
