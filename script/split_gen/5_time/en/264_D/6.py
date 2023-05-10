def main():
    s = input()
    t = 'atcoder'
    n = len(s)
    dp = [[0 for _ in range(len(t)+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(len(t)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
    print(dp[n][len(t)])
