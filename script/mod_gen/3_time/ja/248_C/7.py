def main():
    #入力
    N, M, K = map(int, input().split())
    #初期化
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    mod = 998244353
    #初期条件
    dp[0][0][0] = 1
    #DP
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                #i番目の整数をjにする場合
                if k+j <= K:
                    dp[i+1][j][k+j] += dp[i][j][k]
                    dp[i+1][j][k+j] %= mod
                #i番目の整数をj以外にする場合
                dp[i+1][j][k] += dp[i][j][k] * j
                dp[i+1][j][k] %= mod
    #出力
    print(sum(dp[N][i][K] for i in range(1, M+1)) % mod)

if __name__ == '__main__':
    main()