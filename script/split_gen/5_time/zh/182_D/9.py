def calc_max_coord(n, a):
    max_coord = 0
    cur_coord = 0
    for i in range(n):
        cur_coord += a[i]
        if cur_coord > max_coord:
            max_coord = cur_coord
    return max_coord
