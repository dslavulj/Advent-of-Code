with open('6.txt') as file:
    lines = file.readlines()

lanternfish = list(map(int, lines[0].split(',')))

for i in range(80):
    extra = 0
    for j in range(len(lanternfish)):
        if lanternfish[j] == 0:
            lanternfish[j] = 6
            extra += 1
        else:
            lanternfish[j] -= 1
    for j in range(extra):
        lanternfish.append(8)

print(len(lanternfish))
