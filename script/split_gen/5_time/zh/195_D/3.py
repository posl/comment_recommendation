def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for L, R in Query:
        X_ = X[:L-1]+X[R:]
        X_.sort()
        WV_ = sorted(WV, key=lambda x: x[1], reverse=True)
        ans = 0
        for w, v in WV_:
            for i, x in enumerate(X_):
                if w <= x:
                    X_.pop(i)
                    ans += v
                    break
        print(ans)
