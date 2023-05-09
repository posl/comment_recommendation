def main():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    dp = [[0] * 9 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(9):
            if j == 0:
                dp[i+1][j] = dp[i][j] * 2
            else:
                if s[i] == "chokudai"[j-1]:
                    dp[i+1][j] = dp[i][j] + dp[i][j-1]
                else:
                    dp[i+1][j] = dp[i][j]
    print(dp[n][8] % mod)
main()

if __name__ == '__main__':
    main()