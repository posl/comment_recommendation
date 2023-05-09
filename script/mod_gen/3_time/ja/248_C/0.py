def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod
    print(dp[N][K])

if __name__ == '__main__':
    main()