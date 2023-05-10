def solve():
    s = input()
    t = 'atcoder'
    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
    for i in range(len(t)+1):
        for j in range(len(s)+1):
            if i == 0 or j == 0:
                dp[i][j] = max(i, j)
            else:
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    print(dp[-1][-1])

if __name__ == '__main__':
    solve()