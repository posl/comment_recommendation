def main():
    N = int(input())
    # dp[i][j] := i 桁目まで決めて、その値が j であるような数の個数
    dp = [[0] * 10 for _ in range(N+1)]
    # 1 桁目まで決めて、その値が j であるような数の個数
    dp[1][1] = 1
    dp[1][2] = 1
    dp[1][3] = 1
    dp[1][4] = 1
    dp[1][5] = 1
    dp[1][6] = 1
    dp[1][7] = 1
    dp[1][8] = 1
    dp[1][9] = 1
    # 2 桁目以降を決めていく
    for i in range(2, N+1):
        # j は 1 桁目の値
        for j in range(1, 10):
            # k は 2 桁目の値
            for k in range(1, 10):
                # 1 桁目の値と 2 桁目の値の差が 1 以下であるような場合のみ dp を更新する
                if abs(j-k) <= 1:
                    dp[i][k] += dp[i-1][j]
                    dp[i][k] %= 998244353
    # 答えは、1 桁目から N 桁目までの値がそれぞれ 1,2,...,9 であるような数の個数の和
    print(sum(dp[N])%998244353)

if __name__ == '__main__':
    main()