def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * (i - 1)) % MOD
    print('
'.join(str(x) for x in dp[N][1:]))

if __name__ == '__main__':
    main()