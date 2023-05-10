def solve():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L-1] + X[R:]
        X_.sort()
        ans = 0
        for i in range(N):
            for j in range(len(X_)-1, -1, -1):
                if W[i] <= X_[j]:
                    ans += V[i]
                    X_.pop(j)
                    break
        print(ans)

if __name__ == '__main__':
    solve()