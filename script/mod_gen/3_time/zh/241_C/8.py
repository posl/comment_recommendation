def check(board, i, j):
    if i + 5 >= len(board) or j + 5 >= len(board[0]):
        return False
    for k in range(i, i+6):
        for l in range(j, j+6):
            if board[k][l] == '.':
                return False
    return True

if __name__ == '__main__':
    check()