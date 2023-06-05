def count_rectangles(n, points):
    count = 0
    x = [0 for i in range(n)]
    y = [0 for i in range(n)]
    for i in range(n):
        x[i] = points[i][0]
        y[i] = points[i][1]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if x[i] < x[j] and y[i] < y[j]:
                if [x[i], y[j]] in points and [x[j], y[i]] in points:
                    count += 1
    return count
