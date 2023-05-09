def count_x(x, y, c):
    count = 0
    for i in range(len(c)):
        if c[i][y] == '#':
            count += 1
    return count
