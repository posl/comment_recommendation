def move_piece(board, piece):
    for i in range(len(board)):
        if board[i] == piece:
            if i == len(board) - 1:
                return board
            elif board[i + 1] == 0:
                board[i + 1] = board[i]
                board[i] = 0
                return board
            else:
                return board
    return board

if __name__ == '__main__':
    move_piece()