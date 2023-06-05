def count_visible_squares(h, w, x, y, square):
    count = 0
    for i in range(y, w):
        if square[x][i] == '#':
            break
        count += 1
    for i in range(y-1, -1, -1):
        if square[x][i] == '#':
            break
        count += 1
    for i in range(x, h):
        if square[i][y] == '#':
            break
        count += 1
    for i in range(x-1, -1, -1):
        if square[i][y] == '#':
            break
        count += 1
    return count - 3
