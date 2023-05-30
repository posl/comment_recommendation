def solve():
    N,M,Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    WV = sorted(WV, key=lambda x: (x[1], x[0]), reverse=True)
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for L,R in Query:
        X_ = X[:L-1] + X[R:]
        X_ = sorted(X_)
        ans = 0
        for w,v in WV:
            for i in range(len(X_)):
                if X_[i] >= w:
                    ans += v
                    X_.pop(i)
                    break
        print(ans)
solve()
