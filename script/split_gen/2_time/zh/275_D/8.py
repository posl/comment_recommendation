def main():
    board = [input() for _ in range(9)]
    count = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == '#':
                count += 1
    print(count)
