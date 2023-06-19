def main():
    board = []
    for i in range(9):
        board.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == '#':
                if i-1 >= 0 and j-1 >= 0:
                    if board[i-1][j-1] == '#':
                        if i-1 >= 0 and j+1 < 9:
                            if board[i-1][j+1] == '#':
                                if i+1 < 9 and j+1 < 9:
                                    if board[i+1][j+1] == '#':
                                        if i+1 < 9 and j-1 >= 0:
                                            if board[i+1][j-1] == '#':
                                                count += 1
    print(count)
