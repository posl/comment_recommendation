def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    for L, R in query:
        X_ = X[:L-1] + X[R:]
        X_ = sorted(X_)
        ans_ = 0
        for i in range(N):
            W, V = WV[i]
            for j in range(len(X_)):
                if W <= X_[j]:
                    ans_ += V
                    X_.pop(j)
                    break
        ans.append(ans_)
    return ans
