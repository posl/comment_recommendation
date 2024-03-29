def main():
    s = input()
    t = "atcoder"
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(1,len(s)+1):
        dp[i][0] = i
    for j in range(1,len(t)+1):
        dp[0][j] = j
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(min(dp[i][j-1]+1,dp[i-1][j]+1),dp[i-1][j-1]+1)
    print(dp[len(s)][len(t)])
