with open('4.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]
numbers = lines[0].split(',')
boards = []
idx = 0
for i in range(1, len(lines)):
    if lines[i] == '':
        boards.append([])
        boards[idx].append(lines[i+1].split())
        boards[idx].append(lines[i+2].split())
        boards[idx].append(lines[i+3].split())
        boards[idx].append(lines[i+4].split())
        boards[idx].append(lines[i+5].split())
        idx += 1

def win(board):
    done = False
    nums = []
    for i in range(5):
        pi = 0
        pj = 0
        for j in range(5):
            if board[i][j][-1] == '+':
                pi += 1
            if board[j][i][-1] == '+':
                pj += 1
        if pi == 5:
            done = True
            nums = board[i]
        if pj == 5:
            done = True
            nums = board[:][j]

        if done:
            break
    return done, board

def checknum(board, n):
    for i in range(5):
        for j in range(5):
            if board[i][j] == n:
                board[i][j] += '+'
wboards = []
idxs = []
for i in range(len(numbers)):
    for j in range(len(boards)):
        if boards[j] not in wboards:
            checknum(boards[j], numbers[i])
            done, board = win(boards[j])
            idx = int(numbers[i])
            if done == True:
                wboards.append(board)
                idxs.append(idx)

print(wboards[-1][0], wboards[-1][1])
board, idxs = wboards[-1], idxs[-1]
sum = 0
for i in range(5):
    for j in range(5):
        if board[i][j][-1] != '+':
            sum += int(board[i][j])

print(sum * idx)
