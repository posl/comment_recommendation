def main():
    A, B, Q = map(int, input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        si = bisect.bisect_left(s, x[i])
        ti = bisect.bisect_left(t, x[i])
        ans = 10**20
        for a in [s[si-1], s[si]]:
            for b in [t[ti-1], t[ti]]:
                ans = min(ans, max(a, b)-x[i], x[i]-min(a, b))
        print(ans)
