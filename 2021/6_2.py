with open('6.txt') as file:
    lines = file.readlines()

lanternfish = list(map(int,lines[0].split(',')))
fish_number = [0 for i in range(9)]

for i in range(9):
    fish_number[i] += lanternfish.count(i)


for i in range(256):
    x = fish_number[0]
    for j in range(1,9):
        fish_number[j-1] = fish_number[j]
    fish_number[6] += x
    fish_number[8] = x

print(sum(fish_number))
