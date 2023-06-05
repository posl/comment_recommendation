def find_next(n, m, a, b):
    next = [0] * (n+1)
    for i in range(1, n+1):
        next[i] = i
    for i in range(m):
        if next[a[i]] > next[b[i]]:
            next[a[i]], next[b[i]] = next[b[i]], next[a[i]]
    return next
