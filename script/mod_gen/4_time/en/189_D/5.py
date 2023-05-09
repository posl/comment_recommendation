def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, n+1):
        if s[i-1] == 'AND':
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][0] + 2*dp[i-1][1]
        else:
            dp[i][0] = 2*dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][1]
    print(dp[n][1])

if __name__ == '__main__':
    solve()