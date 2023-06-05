def check_even(h,w,board):
    even_count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] % 2 == 0:
                even_count += 1
    return even_count
