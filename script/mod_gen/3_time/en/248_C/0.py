def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if k + j <= K:
                    dp[i + 1][k + j] += dp[i][j]
                    dp[i + 1][k + j] %= MOD
    print(dp[-1][-1])

if __name__ == '__main__':
    main()