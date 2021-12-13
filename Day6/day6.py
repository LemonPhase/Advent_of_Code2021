# f = open("D:\A level\Computer Science\Programming\Python\Advent of Code\Day6\day6_input.txt", 'r')

# # Making a list for starting numbers
# for line in f:
#     init = list(line.split(","))
# init = list(map(int, init))

# finl = init
# for i in range(256):
#     for index in range(len(finl)):
#         if finl[index] == 0:
#             finl[index] = 6
#             finl.append(8)
#         else:
#             finl[index] -= 1
# print(len(finl))


f = open(
    "D:\A level\Computer Science\Programming\Python\Advent of Code\Day6\day6_input.txt", "r")
data = [int(i) for i in f.read().split(',')]
f.close()
arr = [0 for i in range(9)]

for i in data:
    arr[i] += 1

for i in range(256):
    births = arr.pop(0)
    arr.append(births)
    arr[6] += births
    print(arr)

print(sum(arr))
