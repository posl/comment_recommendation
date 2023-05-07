def main():
    s = input()
    mod = 10**9 + 7
    dp = [[0] * 13 for _ in range(len(s) + 1)]
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(10):
            if s[i] == '?' or s[i] == str(j):
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
                    dp[i+1][(k*10+j)%13] %= mod
    print(dp[len(s)][5])

if __name__ == '__main__':
    main()