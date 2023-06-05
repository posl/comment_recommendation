def solve():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    INF = 10 ** 18
    S = [-INF] + S + [INF]
    T = [-INF] + T + [INF]
    from bisect import bisect_left
    for _ in range(Q):
        x = int(input())
        ans = INF
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        for S1 in [S[s - 1], S[s]]:
            for T1 in [T[t - 1], T[t]]:
                d1 = abs(S1 - x) + abs(T1 - S1)
                d2 = abs(T1 - x) + abs(S1 - T1)
                ans = min(ans, d1, d2)
        print(ans)
