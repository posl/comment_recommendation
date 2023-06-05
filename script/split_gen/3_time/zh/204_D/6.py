def solve(n, t):
    t.sort()
    if n == 1:
        return t[0]
    elif n == 2:
        return max(t)
    else:
        t1 = t.pop()
        t2 = t.pop()
        t3 = t.pop()
        t4 = t.pop()
        return t1 + min(t2, t3, t4) + solve(n - 1, t)
