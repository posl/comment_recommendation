def main():
    #入力
    N, M, K = map(int, input().split())
    #初期値
    mod = 998244353
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    dp[0][0] = 1
    #DP
    for i in range(1, N+1):
        for j in range(1, K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod
    #出力
    print(dp[N][K])

if __name__ == '__main__':
    main()