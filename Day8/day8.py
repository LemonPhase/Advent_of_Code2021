import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

f = open("day8_input.txt", 'r')
f = open("day8_sample_input.txt", 'r')  # 26, 61229
entry_lst = [i.split('|') for i in f.read().splitlines()]
f.close()

print(entry_lst)

# Part1
count = 0
for i in entry_lst:
    i = i[1].split()
    for n in i:
        length = len(n)
        if length in [2, 3, 4, 7]:
            count += 1

print(count)

num_map = {}
# Determine the char for '1' and '7', the extra char 7 has is top

for l in entry_lst:
    n_lst = l[0].split()
    print(n_lst)

    # First operation: determine unique numbers, '1', '4', '7', and '8'
    for n in n_lst:
        length = len(n)
        if length == 2:  # '1'
            num_1 = n
        elif length == 4:  # '4'
            num_4 = n
        elif length == 3:  # '7'
            num_7 = n
        elif length == 7:  # '8'
            num_8 = n
    num_map["top"] = str([x for x in num_7 if x not in num_1])
    # '2', '3', '5' length = 5
    # '0', '6', '9' length = 6

    # '-' as in must contain
    # length 6 - ('4' + top)

    print(num_map)
