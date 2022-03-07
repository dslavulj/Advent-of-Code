with open('2.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]

horizontal_position, depth = 0, 0

for i in range(len(lines)):
    x = int(lines[i][-1])
    if lines[i][0] == 'f':
        horizontal_position += x
    elif lines[i][0] == 'u':
        depth -= x
    elif lines[i][0] == 'd':
        depth += x

print(horizontal_position*depth)