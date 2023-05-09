def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        Y = X[:L-1] + X[R:]
        Y.sort()
        ans = 0
        for j in range(N):
            for k in range(len(Y)):
                if Y[k] >= W[j]:
                    ans += V[j]
                    Y[k] = 0
                    break
        print(ans)
