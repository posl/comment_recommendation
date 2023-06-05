def count(x, y, r):
    x1 = int(x - r)
    x2 = int(x + r)
    y1 = int(y - r)
    y2 = int(y + r)
    cnt = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r:
                cnt += 1
    return cnt
