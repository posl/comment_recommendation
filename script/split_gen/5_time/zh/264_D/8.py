def main():
    s = input()
    t = 'atcoder'
    l = len(s)
    dp = [[0 for _ in range(7)] for _ in range(l)]
    for i in range(l):
        for j in range(7):
            if s[i] != t[j]:
                if i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + 1
            else:
                if i == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]
    print(dp[l-1][6])
