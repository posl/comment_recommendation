def main():
    N = int(input())
    S = [input() for i in range(N)]
    # 0, 1, 2, ... , N
    # 0 = True, 1 = False
    # 0 = AND, 1 = OR
    # 0 = True, 1 = False
    dp = [[[0 for i in range(2)] for j in range(2)] for k in range(N + 1)]
    # initial value
    dp[0][0][0] = 1
    dp[0][1][0] = 1
    for i in range(N):
        if S[i] == 'AND':
            dp[i + 1][0][0] += dp[i][0][0]
            dp[i + 1][0][1] += dp[i][0][0] + dp[i][0][1] + dp[i][1][0] + dp[i][1][1]
            dp[i + 1][1][1] += dp[i][1][1]
        else:
            dp[i + 1][0][0] += dp[i][0][0] + dp[i][0][1] + dp[i][1][0] + dp[i][1][1]
            dp[i + 1][1][0] += dp[i][1][0]
            dp[i + 1][1][1] += dp[i][1][0] + dp[i][1][1]
    print(dp[N][0][0] + dp[N][0][1] + dp[N][1][0] + dp[N][1][1])

if __name__ == '__main__':
    main()