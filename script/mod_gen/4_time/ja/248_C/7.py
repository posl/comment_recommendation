def main():
    # 標準入力受け取り
    n, m, k = map(int, input().split())
    # 2次元配列を初期化
    dp = [[0] * (k+1) for i in range(n+1)]
    # 1次元目を初期化
    for i in range(1, m+1):
        if i <= k:
            dp[1][i] = 1
    # 2次元目以降を初期化
    for i in range(2, n+1):
        for j in range(1, k+1):
            # 1次元目の配列を足す
            dp[i][j] = dp[i-1][j]
            # 2次元目の配列を足す
            for l in range(1, m+1):
                if j-l >= 0:
                    dp[i][j] += dp[i-1][j-l]
                    dp[i][j] %= 998244353
    print(dp[n][k])

if __name__ == '__main__':
    main()