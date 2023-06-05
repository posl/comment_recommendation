def main():
    board = [input() for _ in range(9)]
    cnt = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == '#':
                cnt += 1
    print(cnt)
