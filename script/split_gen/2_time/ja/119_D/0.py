def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        s = bisect.bisect_left(S, x)
        t = bisect.bisect_left(T, x)
        ans = float('inf')
        for s1 in [S[s-1], S[s]]:
            for t1 in [T[t-1], T[t]]:
                d1 = abs(s1 - x) + abs(t1 - s1)
                d2 = abs(t1 - x) + abs(s1 - t1)
                ans = min(ans, d1, d2)
        print(ans)
