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
        X_copy = X[:L-1] + X[R:]
        X_copy.sort()
        ans = 0
        for i in range(N):
            for j in range(len(X_copy)):
                if W[i] <= X_copy[j]:
                    ans += V[i]
                    X_copy.pop(j)
                    break
        print(ans)
