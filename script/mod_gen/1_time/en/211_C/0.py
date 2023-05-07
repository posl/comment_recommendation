def main():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    dp = [[0] * 9 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(9):
            if s[i] == "chokudai"[j]:
                dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
            else:
                dp[i+1][j+1] = dp[i][j+1] % mod
    print(dp[n][8])

if __name__ == '__main__':
    main()