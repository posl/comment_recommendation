def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(N+1):
            if j == 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            else:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + X[i])
                if j >= C[i]:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j-C[i]] + Y[i])
    print(max(dp[N]))
