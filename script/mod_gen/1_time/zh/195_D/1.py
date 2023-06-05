def solve():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        X_ = X[:L] + X[R+1:]
        X_.sort()
        ans = 0
        for j in range(1 << len(X_)):
            x = 0
            for k in range(len(X_)):
                if j >> k & 1:
                    x += X_[k]
            w = 0
            for k in range(N):
                if x >= W[k] and x <= X[k]:
                    w += V[k]
            ans = max(ans, w)
        print(ans)
solve()
