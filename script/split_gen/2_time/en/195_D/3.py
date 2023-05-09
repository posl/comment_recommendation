def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        #print(L, R)
        X_ = X[0:L-1] + X[R:]
        #print(X_)
        ans = 0
        for j in range(2 ** N):
            s = 0
            v = 0
            for k in range(N):
                if (j >> k) & 1:
                    s += W[k]
                    v += V[k]
            for x in X_:
                if s <= x:
                    ans = max(ans, v)
                    break
        print(ans)
