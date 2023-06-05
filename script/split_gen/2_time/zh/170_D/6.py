def find_nearest_int(x, n, p):
    min_diff = 100
    nearest_int = 0
    for i in range(1, 101):
        if i not in p:
            diff = abs(x - i)
            if diff < min_diff:
                min_diff = diff
                nearest_int = i
    return nearest_int
