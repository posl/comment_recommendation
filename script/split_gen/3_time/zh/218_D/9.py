def solve(n, points):
    x = {}
    y = {}
    for p in points:
        if p[0] not in x:
            x[p[0]] = 1
        else:
            x[p[0]] += 1
        if p[1] not in y:
            y[p[1]] = 1
        else:
            y[p[1]] += 1
    ans = 0
    for p in points:
        ans += (x[p[0]] - 1) * (y[p[1]] - 1)
    return ans
