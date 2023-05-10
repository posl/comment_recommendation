def solve(n, t):
    t.sort()
    t.reverse()
    a = 0
    b = 0
    for i in range(n):
        if a > b:
            b += t[i]
        else:
            a += t[i]
    return max(a, b)
