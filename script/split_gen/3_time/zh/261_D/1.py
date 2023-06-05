def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for _ in range(M)]
    CY.sort(key=lambda x: x[1], reverse=True)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + 1 == CY[0][0]:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + CY[0][1])
            elif j + 1 > CY[0][0]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + CY[0][1])
    print(max(max(dp)))
