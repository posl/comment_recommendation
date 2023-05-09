def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j]: i桁目まで見て、mod jでの値がkになる数
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(10):
            dp[i][j] = dp[i - 1][j] * 2
            dp[i][(j + A[i - 1]) % 10] += dp[i - 1][j]
            dp[i][(j * A[i - 1]) % 10] += dp[i - 1][j]
            dp[i][j] %= MOD
    for i in range(10):
        print(dp[N][i])
