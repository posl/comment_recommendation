def main():
    S = int(input())
    # dp[i][j] i個の整数でjを作るパターン数
    dp = [[0 for _ in range(S+1)] for _ in range(2001)]
    dp[0][0] = 1
    for i in range(1, 2001):
        for j in range(S+1):
            if j - i >= 0:
                dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % (10**9 + 7)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[2000][S])

if __name__ == '__main__':
    main()