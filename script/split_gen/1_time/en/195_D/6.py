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
        X2 = X[:L - 1] + X[R:]
        X2.sort()
        V2 = sorted(zip(V, W), reverse=True)
        ans = 0
        for v, w in V2:
            for j in range(len(X2)):
                if X2[j] >= w:
                    ans += v
                    X2[j] = 0
                    break
        print(ans)
