from abc import abstractproperty
import statistics
f = open("D:\A level\Computer Science\Programming\Python\Advent of Code\Day7\day7_input.txt", 'r')

for line in f:
    pos = list(line.split(","))
f.close()

pos = list(map(int, pos))
print(pos)
mean = round(statistics.mean(pos))
mode = round((statistics.mode(pos)))
median = round((statistics.median(pos)))


def fuel_calc_1(n):
    fuel = 0
    for crab in pos:
        fuel += abs(crab - n)
    return fuel


def fuel_calc_2(n):
    fuel = 0
    for crab in pos:
        # 1/2n(n+1)
        fuel += round((abs(crab - n) + 1) * abs(crab - n) / 2)
    return fuel


def part1():
    print(fuel_calc_1(mean), fuel_calc_1(mode), fuel_calc_1(median))


def part2():
    print(fuel_calc_2(mean), fuel_calc_2(mode), fuel_calc_2(median))
    print(fuel_calc_2(499))
    print(fuel_calc_2(500))
    print(fuel_calc_2(501))


part2()

print(mean)
