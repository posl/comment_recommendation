def main():
    s = input()
    t = 'atcoder'
    n = len(s)
    m = len(t)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j-1]+1,
                    dp[i-1][j]+1,
                    dp[i][j-1]+1
                )
    print(dp[n][m])

if __name__ == '__main__':
    main()