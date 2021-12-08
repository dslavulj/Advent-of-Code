with open('5.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]

coords = []
for line in lines:
    coords.append(line.split(' -> '))
for i in range(len(coords)):
    for j in range(2):
        coords[i][j] = list(map(int, coords[i][j].split(',')))

diagram = [[0 for i in range(1000)] for j in range(1000)]


def filldia(x1, x2, y1, y2):
    if x1 == x2:
        begin, end = min(y1, y2), max(y1, y2)
        for i in range(begin, end + 1):
            diagram[i][x1] += 1
    elif y1 == y2:
        begin, end = min(x1, x2), max(x1, x2)
        for i in range(begin, end + 1):
            diagram[y1][i] += 1
    else:
        while True:
            diagram[y1][x1] += 1
            if x1 == x2 and y1 == y2:
                break
            x1 += 1 if x2 > x1 else -1
            y1 += 1 if y2 > y1 else -1


for i in range(len(coords)):
    filldia(coords[i][0][0], coords[i][1][0], coords[i][0][1], coords[i][1][1])

c = 0
for i in range(len(diagram)):
    for j in range(len(diagram[i])):
        if diagram[i][j] >= 2:
            c += 1
print(c)
