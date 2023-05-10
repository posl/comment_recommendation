def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    S = [-10**11] + S + [10**11]
    T = [-10**11] + T + [10**11]
    from bisect import bisect_left, bisect_right
    def solve(x):
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        res = 10**11
        for s0 in [S[s-1], S[s]]:
            for t0 in [T[t-1], T[t]]:
                d1 = abs(x-s0) + abs(s0-t0)
                d2 = abs(x-t0) + abs(t0-s0)
                res = min(res, d1, d2)
        return res
    for x in X:
        print(solve(x))
