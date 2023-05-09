def calc(n, k, a):
    if k >= n:
        return [k//n]*n
    else:
        a.sort()
        r = [0]*n
        for i in range(k):
            r[a[i]-1] += 1
        return r
