def main():
    A, B, Q = map(int, input().split())
    S = [-float('inf')] + [int(input()) for _ in range(A)] + [float('inf')]
    T = [-float('inf')] + [int(input()) for _ in range(B)] + [float('inf')]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        s = bisect.bisect_right(S, x)
        t = bisect.bisect_right(T, x)
        ans = float('inf')
        for si in [s - 1, s]:
            for ti in [t - 1, t]:
                ans = min(ans, max(S[si], T[ti]) - x, x - min(S[si], T[ti]))
                ans = min(ans, abs(S[si] - x) + abs(T[ti] - S[si]))
                ans = min(ans, abs(T[ti] - x) + abs(S[si] - T[ti]))
        print(ans)
