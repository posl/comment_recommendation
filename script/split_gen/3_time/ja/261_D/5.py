def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [0] * (N+1)
    dp[0] = X[0]
    for i in range(1, N):
        dp[i] = dp[i-1] + X[i]
        for j in range(M):
            if i + 1 - C[j] >= 0:
                dp[i] = max(dp[i], dp[i-C[j]] + Y[j])
    print(dp[N-1])
