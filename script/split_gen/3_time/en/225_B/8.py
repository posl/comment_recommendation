def isStar(n, a, b):
    if n-1 != len(a) or n-1 != len(b):
        return False
    if n == 3:
        return True
    c = [0 for i in range(n)]
    for i in range(n-1):
        c[a[i]-1] += 1
        c[b[i]-1] += 1
    for i in range(n):
        if c[i] == n-1:
            return True
    return False
