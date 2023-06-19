def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.append(10**11)
    t.append(10**11)
    from bisect import bisect_left, bisect_right
    for i in range(Q):
        j = bisect_left(s, x[i])
        k = bisect_left(t, x[i])
        ans = 10**11
        for sj in [s[j-1], s[j]]:
            for tk in [t[k-1], t[k]]:
                ans = min(ans, abs(sj-x[i])+abs(tk-sj), abs(tk-x[i])+abs(sj-tk))
        print(ans)
main()
