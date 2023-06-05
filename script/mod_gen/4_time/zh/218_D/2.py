def calc_rects(n, points):
    rects = 0
    for i in range(n):
        for j in range(i+1, n):
            p1 = points[i]
            p2 = points[j]
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue
            p3 = (p1[0], p2[1])
            p4 = (p2[0], p1[1])
            if p3 in points and p4 in points:
                rects += 1
    return rects

if __name__ == '__main__':
    calc_rects()