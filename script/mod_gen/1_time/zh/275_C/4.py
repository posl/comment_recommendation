def get_square_count():
    chessboard = []
    for i in range(9):
        chessboard.append(input())
    count = 0
    for r in range(8):
        for c in range(8):
            if chessboard[r][c] == '#' and chessboard[r][c+1] == '#' and chessboard[r+1][c] == '#' and chessboard[r+1][c+1] == '#':
                count += 1
    print(count)
get_square_count()
