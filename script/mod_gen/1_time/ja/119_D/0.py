def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    import bisect
    ss = [-float("inf")] + s + [float("inf")]
    tt = [-float("inf")] + t + [float("inf")]
    for xx in x:
        i = bisect.bisect_right(ss, xx)
        j = bisect.bisect_right(tt, xx)
        res = float("inf")
        for s1 in [ss[i - 1], ss[i]]:
            for t1 in [tt[j - 1], tt[j]]:
                d1 = abs(xx - s1) + abs(s1 - t1)
                d2 = abs(xx - t1) + abs(t1 - s1)
                res = min(res, d1, d2)
        print(res)

if __name__ == '__main__':
    main()