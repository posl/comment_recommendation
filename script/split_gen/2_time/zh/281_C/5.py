def getSong(t, a):
    num = len(a)
    t = t % sum(a)
    for i in range(num):
        if t < a[i]:
            return i+1, t
        t -= a[i]
    return -1, -1
