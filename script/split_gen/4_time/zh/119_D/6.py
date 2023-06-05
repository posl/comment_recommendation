def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    inf = 10 ** 18
    s = [-inf] + s + [inf]
    t = [-inf] + t + [inf]
    import bisect
    for i in x:
        si = bisect.bisect_left(s, i)
        ti = bisect.bisect_left(t, i)
        ans = inf
        for ss in [s[si - 1], s[si]]:
            for tt in [t[ti - 1], t[ti]]:
                d = min(abs(i - ss), abs(i - tt))
                d += abs(ss - tt)
                ans = min(ans, d)
        print(ans)
