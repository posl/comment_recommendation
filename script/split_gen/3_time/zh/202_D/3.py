def comb(n, m):
    if n == m or m == 0:
        return 1
    elif 0 < m < n:
        return comb(n-1, m-1) + comb(n-1, m)
    else:
        return 0
