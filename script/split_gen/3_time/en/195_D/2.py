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
        X_tmp = X[:L-1] + X[R:]
        X_tmp.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X_tmp)):
                if X_tmp[k] >= W[j]:
                    ans += V[j]
                    X_tmp[k] = 0
                    break
        print(ans)
