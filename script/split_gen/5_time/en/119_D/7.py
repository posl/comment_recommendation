def main():
    import bisect
    INF = 10**18
    A, B, Q = map(int, input().split())
    S = [-INF] + [int(input()) for _ in range(A)] + [INF]
    T = [-INF] + [int(input()) for _ in range(B)] + [INF]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        s, t = bisect.bisect_left(S, x), bisect.bisect_left(T, x)
        ans = INF
        for s0 in [S[s-1], S[s]]:
            for t0 in [T[t-1], T[t]]:
                ans = min(ans, abs(s0 - x) + abs(s0 - t0), abs(t0 - x) + abs(s0 - t0))
        print(ans)
