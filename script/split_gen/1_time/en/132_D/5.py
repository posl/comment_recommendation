def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for i in range(K):
        for j in range(N):
            dp[i + 1][j + 1] = (dp[i + 1][j] + dp[i][j]) % MOD
    ans = [0] * (K + 1)
    for i in range(K + 1):
        ans[i] = dp[i][N] * dp[K - i][N] % MOD
    for i in range(1, K + 1):
        ans[i] = (ans[i] - ans[i - 1]) % MOD
    print('
'.join(map(str, ans[1:])))
