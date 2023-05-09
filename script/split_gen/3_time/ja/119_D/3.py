def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    for i in range(Q):
        x = X[i]
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        ans = 10**20
        for ss in (S[max(0, s-1)], S[min(A-1, s)]):
            for tt in (T[max(0, t-1)], T[min(B-1, t)]):
                d1 = abs(ss - x) + abs(tt - ss)
                d2 = abs(tt - x) + abs(ss - tt)
                ans = min(ans, d1, d2)
        print(ans)
