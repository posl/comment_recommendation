def f(n, k, a):
    if k <= n:
        return a[k-1]
    else:
        k = k % n
        if k == 0:
            return a[n-1]
        else:
            return a[k-1]
