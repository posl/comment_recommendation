def solve():
    N, M, Q = map(int, input().split())
    WV = [tuple(map(int, input().split())) for _ in range(N)]
    WV.sort(key=lambda x: x[1], reverse=True)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L - 1] + X[R:]
        X_.sort()
        ans = 0
        for w, v in WV:
            for i, x in enumerate(X_):
                if w <= x:
                    ans += v
                    X_.pop(i)
                    break
        print(ans)

if __name__ == '__main__':
    solve()