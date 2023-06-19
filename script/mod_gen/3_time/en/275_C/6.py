def countSquares():
    board = []
    for i in range(9):
        board.append(input())
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#' and board[i+1][j] == '#' and board[i][j+1] == '#' and board[i+1][j+1] == '#':
                count += 1
    print(count)
countSquares()
