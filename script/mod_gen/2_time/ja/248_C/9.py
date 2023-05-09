def main():
    #入力
    N, M, K = map(int, input().split())
    #N ≦ K ≦ NM
    #dp[i][j] = i個の数列で、sum _{i=1}^N A_i ≦ j となる数列の個数
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            if j - M - 1 >= 0:
                dp[i][j] -= dp[i-1][j-M-1]
            dp[i][j] %= 998244353
    print(dp[N][K])

if __name__ == '__main__':
    main()