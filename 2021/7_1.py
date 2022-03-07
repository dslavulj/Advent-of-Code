import numpy as np
with open('7.txt') as file:
    lines = file.readlines()

positions = list(map(int,lines[0].split(',')))

median = np.median(positions)
fuel = 0
for position in positions:
    fuel += (abs(position-median))

print(int(fuel))