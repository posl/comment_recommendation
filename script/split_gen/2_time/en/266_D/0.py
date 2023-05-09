def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[0] * 5 for i in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if T[i] - j >= 0:
                dp[i + 1][X[i]] = max(dp[i + 1][X[i]], dp[i][j] + A[i])
    ans = 0
    for i in range(5):
        ans = max(ans, dp[N][i])
    print(ans)
