f = open("D:\A level\Computer Science\Programming\Python\Advent of Code\Day2_input.txt", 'r')


def part1():
    procedure = {'forward': 0, 'down': 0, 'up': 0}
    for line in f:
        line.strip('\n')
        key, value = line.split()
        procedure[key] += int(value)
    print(procedure)
    print(procedure['forward'] * (procedure['up'] - procedure['down']))


def part2():
    position = {'horizontal': 0, 'depth': 0, 'aim': 0}
    for line in f:
        line.strip('\n')
        direction, value = line.split()
        value = int(value)
        if direction == 'forward':
            position['horizontal'] += value
            position['depth'] += position['aim'] * value
        elif direction == 'up':
            position['aim'] += value
        elif direction == 'down':
            position['aim'] -= value
    print(position)
    print(position['horizontal'] * position['depth'])


part2()

f.close()
# This not the best way, do better next week
