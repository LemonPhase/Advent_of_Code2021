f = open("D:\A level\Computer Science\Programming\Python\Advent of Code\Day1_input.txt", 'r')
depth = []
for x in f:
    depth.append(int(x.strip('\n')))
f.close()


def part1():
    # depth = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    counter = 0

    for i in range(len(depth) - 1):
        if depth[i] < depth[i + 1]:
            counter += 1
        else:
            continue

    print(counter)


def part2():
    # depth = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    counter = 0

    for i in range(len(depth) - 3):
        if sum(depth[i: i + 3]) < sum(depth[i + 1: i + 4]):
            counter += 1
        else:
            continue

    print(counter)


print(depth[0: 2])

part2()
