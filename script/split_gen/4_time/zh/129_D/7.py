def get_squares(row,col):
    squares = 0
    for i in range(row):
        if i == 0 or i == row - 1:
            squares += col
        else:
            squares += 2
    return squares
