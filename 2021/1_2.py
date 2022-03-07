with open('1.txt') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

c = 0

for i in range(1, len(lines)-2):
    if lines[i-1]+lines[i]+lines[i+1] < lines[i]+lines[i+1]+lines[i+2]:
        c += 1

print(c)
