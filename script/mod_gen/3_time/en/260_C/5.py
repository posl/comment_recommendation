def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #dp[i][j] = i番目の宝石をj個の宝石に変換するときの最大値
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            dp[i][j] = max(dp[i][j], dp[i][j+1] + X)
            dp[i][j] = max(dp[i][j], dp[i+1][j] + Y)
    print(dp[0][0])

if __name__ == '__main__':
    main()