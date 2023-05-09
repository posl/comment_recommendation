def main():
    s = input()
    n = len(s)
    dp = [[float('inf') for _ in range(2)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(2):
            if j == 0:
                dp[i+1][1] = min(dp[i+1][1], dp[i][j] + 1)
            else:
                dp[i+1][0] = min(dp[i+1][0], dp[i][j] + 1)
            if j == 0:
                if s[i] == '0':
                    dp[i+1][0] = min(dp[i+1][0], dp[i][j])
                else:
                    dp[i+1][1] = min(dp[i+1][1], dp[i][j])
            else:
                if s[i] == '0':
                    dp[i+1][1] = min(dp[i+1][1], dp[i][j] + 1)
                else:
                    dp[i+1][0] = min(dp[i+1][0], dp[i][j] + 1)
    print(min(dp[n][0], dp[n][1]))
