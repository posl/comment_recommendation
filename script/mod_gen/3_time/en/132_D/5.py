def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    for i in range(K + 1):
        for j in range(N + 1):
            if i == 0:
                dp[i][j] = 0
            elif i == 1:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) % mod
    for i in range(1, K + 1):
        print((dp[i][N] * dp[K - i + 1][N]) % mod)

if __name__ == '__main__':
    main()