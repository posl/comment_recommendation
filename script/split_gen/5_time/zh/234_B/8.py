def max_len(n, points):
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n):
            len = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if len > max_len:
                max_len = len
    return max_len ** 0.5
