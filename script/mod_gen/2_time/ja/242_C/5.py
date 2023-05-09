def main():
    N = int(input())
    # dp[i][j] = i桁目まで見て、jで終わる数の個数
    dp = [[0 for _ in range(10)] for _ in range(N)]
    # 1桁目は1から9までの数が1通りずつある
    for i in range(10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][0] = dp[i-1][1]
            elif j == 9:
                dp[i][9] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[N-1]) % 998244353)

if __name__ == '__main__':
    main()