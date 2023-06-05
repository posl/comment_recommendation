def main():
    s = input()
    s = s[::-1]
    t = "chokudai"[::-1]
    mod = 10**9+7
    dp = [[0]*9 for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(9):
            if s[i] != t[j]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = (dp[i][j] + dp[i][j-1]) % mod
    print(dp[-1][-1])
