def cumsum(a):
    s = 0
    res = []
    for i in range(len(a)):
        s += a[i]
        res.append(s)
    return res
