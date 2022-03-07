import numpy as np

with open('7.txt') as file:
    lines = file.readlines()

positions = list(map(int, lines[0].split(',')))

mean = int(np.mean(positions))
fuel = 0
for position in positions:
    s = 0
    for i in range(abs(position - mean)):
        s += i + 1
    fuel += s

print(fuel)