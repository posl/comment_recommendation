def count_point(n, d, points):
    count = 0
    for i in range(n):
        if points[i][0]**2 + points[i][1]**2 <= d**2:
            count += 1
    return count
