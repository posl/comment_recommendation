def main():
    n = int(input())
    s = [input() for _ in range(n)]
    dp = [[0] * 2 for _ in range(n+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(n):
        if s[i] == "AND":
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0] + dp[i][1] * 2
        else:
            dp[i+1][0] = dp[i][0] * 2 + dp[i][1]
            dp[i+1][1] = dp[i][1]
    print(dp[n][1])
