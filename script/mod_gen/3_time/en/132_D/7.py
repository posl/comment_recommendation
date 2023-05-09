def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    # dp[i][j]: i個のボールからj個の青いボールを選ぶ方法の数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(min(i, K) + 1):
            dp[i][j] = dp[i - 1][j] * j + dp[i - 1][j - 1] * (i - j)
            dp[i][j] %= MOD
    # ans[i]: i回の操作で青いボールを全て取る方法の数
    ans = [0] * (K + 1)
    for i in range(1, K + 1):
        ans[i] = dp[N][i] * i % MOD
    print('
'.join(map(str, ans[1:])))

if __name__ == '__main__':
    main()