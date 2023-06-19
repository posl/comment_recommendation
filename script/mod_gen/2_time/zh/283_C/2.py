def main():
    S = input()
    N = len(S)
    #dp[i][j]表示第i个数字，输入第j个按键的最小次数
    dp = [[float('inf')] * 11 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(11):
            #如果输入00键
            if j == 0:
                dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            else:
                dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j])
            #如果输入其他键
            if S[i] == str(j):
                dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            else:
                dp[i+1][int(S[i])] = min(dp[i][j] + 1, dp[i+1][int(S[i])])
    print(dp[N][0])

if __name__ == '__main__':
    main()