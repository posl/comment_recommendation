def main():
    s = input()
    atcoder = "atcoder"
    n = len(s)
    dp = [[0 for _ in range(7)] for _ in range(n)]
    for i in range(n):
        for j in range(7):
            if s[i] == atcoder[j]:
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
    if dp[n-1][6] == 0:
        print(-1)
    else:
        print(n - dp[n-1][6])

if __name__ == '__main__':
    main()