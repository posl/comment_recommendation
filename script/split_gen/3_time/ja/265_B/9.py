def func(n, m, t, a, xy):
    for i in range(n-1):
        t -= a[i]
        if t <= 0:
            return False
        for j in range(m):
            if xy[j][0] == i+1:
                t += xy[j][1]
    return True
