with open('3.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]

lines2 = lines.copy()

pos = 0
while True:
    half = len(lines)/2
    count = 0
    ones = []
    zeros = []
    for i in range(len(lines)):
        if lines[i][pos] == '1':
            count += 1
            ones.append(lines[i])
        else:
            zeros.append(lines[i])
    if count >= half:
        lines = ones.copy()
    else:
        lines = zeros.copy()
    pos += 1
    if len(lines) == 1:
        break
oxygen = lines[0]

pos = 0
while True:
    half = len(lines2)/2
    count = 0
    ones = []
    zeros = []
    for i in range(len(lines2)):
        if lines2[i][pos] == '1':
            count += 1
            ones.append(lines2[i])
        else:
            zeros.append(lines2[i])
    if count < half:
        lines2 = ones.copy()
    else:
        lines2 = zeros.copy()
    pos += 1
    if len(lines2) == 1:
        break
CO2 = lines2[0]

score = int(''.join(oxygen), 2) * int(''.join(CO2), 2)
print(score)
