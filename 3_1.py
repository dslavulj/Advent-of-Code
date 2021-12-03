with open('3.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]

counts = [0 for i in range(len(lines[0]))]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '1':
            counts[j] += 1

gamma = ['0' for i in range(len(counts))]
epsilon = ['0' for i in range(len(counts))]
half = int(len(lines)/2)
for i in range(len(counts)):
    if counts[i] > half:
        gamma[i] = '1'
    else:
        epsilon[i] = '1'
score = int(''.join(gamma), 2) * int(''.join(epsilon), 2)
print(score)