def find_square(board):
    # 从左上角开始遍历
    length = len(board)
    result = 0
    for i in range(length):
        for j in range(length):
            if board[i][j] == '#':
                # 从该点出发，遍历右边和下边的所有点
                for k in range(j+1, length):
                    if board[i][k] == '#':
                        for l in range(i+1, length):
                            if board[l][j] == '#' and board[l][k] == '#':
                                result += 1
    return result
