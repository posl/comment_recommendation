def main():
    s = input()
    t = "atcoder"
    l = len(s)
    dp = [[0] * (l+1) for _ in range(8)]
    for i in range(l):
        for j in range(8):
            if s[i] == t[j]:
                if j == 0:
                    dp[j][i+1] = dp[j][i] + 1
                else:
                    dp[j][i+1] = min(dp[j][i] + 1, dp[j-1][i])
            else:
                dp[j][i+1] = dp[j][i]
    print(l - dp[7][l])
