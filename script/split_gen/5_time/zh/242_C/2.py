def main():
    n = int(input())
    m = 998244353
    dp = [[0 for _ in range(9)] for _ in range(n+1)]
    for i in range(1, 10):
        dp[1][i-1] = 1
    for i in range(2, n+1):
        for j in range(9):
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % m
            if j != 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % m
            if j != 8:
                dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % m
    ans = 0
    for i in range(9):
        ans = (ans + dp[n][i]) % m
    print(ans)
