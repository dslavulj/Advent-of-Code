with open('1.txt') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

c = 0

for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        c += 1

print(c)
