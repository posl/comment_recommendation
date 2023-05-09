def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    X = [0] * M
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        #print(N, M, Q)
        #print(W)
        #print(V)
        #print(X)
        #print(L, R)
        X_ = X[:L - 1] + X[R:]
        X_.sort()
        #print(X_)
        ans = 0
        for j in range(N):
            for k in range(len(X_)):
                if W[j] <= X_[k]:
                    ans += V[j]
                    X_[k] = 0
                    break
        print(ans)
