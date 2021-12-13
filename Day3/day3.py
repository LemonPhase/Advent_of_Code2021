from collections import Counter
from os import rmdir
import os
f = open("D:\A level\Computer Science\Programming\Python\Advent of Code\Day3\day3_input.txt", 'r')

report = []
# Make a list for the diagnostic report
for line in f:
    report.append(line.strip('\n'))
f.close()

# Gamma - most occuring bit in that position
gamma = ""
occurrence = []

# Creating a temporary string for the bits in the same position
for pos in range(len(report[0])):
    # Iterate through all positions
    bits_in_pos = ''
    for value in report:
        # Adding the specific bit of that element in that position into the temp string
        bits_in_pos += value[pos]
    # Adding most frequent occuring bit to gamma
    gamma += str(Counter(bits_in_pos).most_common(1)[0][0])
    occurrence.append(Counter(bits_in_pos).most_common())

# Checking occurrence of bits in each position
# print(occurrence)
# print(occurrence[0][0][1])


def rating(gas):
    rmng_value = report

    # Couting the number of 1s and 0s in that position
    for pos in range(len(report[0])):
        count_1 = count_0 = 0
        for value in rmng_value:
            if value[pos] == '1':
                count_1 += 1
            elif value[pos] == '0':
                count_0 += 1

        # Using a temporary list for disred binary value
        temp_rmng = []
        if count_1 > count_0:
            for value in rmng_value:
                if gas == 'oxygen' and value[pos] == '1':
                    temp_rmng.append(value)
                elif gas == 'co2' and value[pos] != '1':
                    temp_rmng.append(value)

        elif count_1 < count_0:
            for value in rmng_value:
                if gas == 'oxygen' and value[pos] == '0':
                    temp_rmng.append(value)
                elif gas == 'co2' and value[pos] != '0':
                    temp_rmng.append(value)

        elif count_1 == count_0:
            for value in rmng_value:
                if gas == 'oxygen' and value[pos] == '1':
                    temp_rmng.append(value)
                elif gas == 'co2' and value[pos] == '0':
                    temp_rmng.append(value)

        rmng_value = temp_rmng
        # print(count_0, count_1)
        # print(rmng_value)

        # Return the list once there's only one value
        # Prevents it to be an empty,
        # as for co2 nothing could be appended as we're taking the less value.
        if len(rmng_value) == 1:
            return rmng_value


def part1():
    epsilon = ""

    # Inverting gamma gets epsilon
    epsilon = gamma.replace('1', '2')
    epsilon = epsilon.replace('0', '1')
    epsilon = epsilon.replace('2', '0')
    print(int(gamma, 2) * int(epsilon, 2))


def part2():
    oxygen = int(rating('oxygen')[0], 2)
    co2 = int(rating('co2')[0], 2)
    print(oxygen, co2, oxygen * co2)


part2()
