def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j]: i番目までの整数の和をjとする選び方の数
    dp = [[0] * (N * 10 ** 9 + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N * 10 ** 9 + 1):
            dp[i + 1][j] += dp[i][j] * 2
            dp[i + 1][j] %= MOD
            if j - A[i] >= 0:
                dp[i + 1][j] += dp[i][j - A[i]]
                dp[i + 1][j] %= MOD
    ans = 0
    for i in range(1, N + 1):
        ans += dp[i][i * sum(A) // N]
        ans %= MOD
    print(ans)
