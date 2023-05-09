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
        W2 = [0] * (M - (R - L + 1))
        V2 = [0] * (M - (R - L + 1))
        X2 = [0] * (M - (R - L + 1))
        j = 0
        for k in range(M):
            if k < L - 1 or k > R - 1:
                W2[j] = W[k]
                V2[j] = V[k]
                X2[j] = X[k]
                j += 1
        dp = [[0 for _ in range(sum(X2) + 1)] for _ in range(M - (R - L + 1) + 1)]
        for k in range(M - (R - L + 1)):
            for l in range(sum(X2) + 1):
                if l >= W2[k]:
                    dp[k + 1][l] = max(dp[k][l - W2[k]] + V2[k], dp[k][l])
                else:
                    dp[k + 1][l] = dp[k][l]
        print(dp[M - (R - L + 1)][sum(X2)])
