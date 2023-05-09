def main():
    s = input()
    t = input()
    n = len(t)
    m = len(s)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s[i]==t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(m-dp[m][n])

if __name__ == '__main__':
    main()