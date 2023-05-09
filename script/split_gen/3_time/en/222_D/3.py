def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            if A[i] <= j:
                dp[i + 1][j] += dp[i + 1][j - 1]
                dp[i + 1][j] %= MOD
            if j <= B[i]:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD
    print(dp[N][N])
