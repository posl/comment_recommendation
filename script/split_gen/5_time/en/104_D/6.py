def main():
    s = input()
    n = len(s)
    MOD = 10 ** 9 + 7
    dp = [[0]*4 for i in range(n+1)]
    dp[n][3] = 1
    for i in range(n-1, -1, -1):
        for j in range(4):
            if s[i] == '?':
                dp[i][j] = 3 * dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j]
            if j < 3 and (s[i] == '?' or s[i] == 'ABC'[j]):
                dp[i][j] += dp[i+1][j+1]
            dp[i][j] %= MOD
    print(dp[0][0])
