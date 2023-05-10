def solve(A, B, Q, s, t, x):
    s = [-float('inf')] + s + [float('inf')]
    t = [-float('inf')] + t + [float('inf')]
    from bisect import bisect_left
    for xi in x:
        si = bisect_left(s, xi)
        ti = bisect_left(t, xi)
        res = float('inf')
        for sj in [s[si - 1], s[si]]:
            for tk in [t[ti - 1], t[ti]]:
                d1 = abs(sj - xi) + abs(tk - sj)
                d2 = abs(tk - xi) + abs(tk - sj)
                res = min(res, d1, d2)
        print(res)
