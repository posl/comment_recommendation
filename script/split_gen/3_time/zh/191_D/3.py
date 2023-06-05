def grid_in_circle(x, y, r):
    x1 = int(x - r)
    x2 = int(x + r)
    y1 = int(y - r)
    y2 = int(y + r)
    count = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                count += 1
    return count
