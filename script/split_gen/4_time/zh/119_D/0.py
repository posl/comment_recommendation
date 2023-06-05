def solve(A, B, Q, s, t, x):
    import bisect
    INF = 10**11
    s = [0] + s + [INF]
    t = [0] + t + [INF]
    for _ in range(Q):
        ans = INF
        xi = x[_]
        s_i = bisect.bisect_right(s, xi)
        t_i = bisect.bisect_right(t, xi)
        for si in [s[s_i-1], s[s_i]]:
            for ti in [t[t_i-1], t[t_i]]:
                d1 = abs(si - xi) + abs(ti - si)
                d2 = abs(ti - xi) + abs(si - ti)
                ans = min(ans, d1, d2)
        print(ans)
