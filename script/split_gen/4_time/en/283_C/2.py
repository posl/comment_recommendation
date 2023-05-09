def main():
    S = input()
    l = len(S)
    dp = [[float("inf")] * 2 for _ in range(l+1)]
    dp[0][0] = 0
    for i in range(l):
        for j in range(2):
            n = int(S[i])
            if j == 1:
                n += 1
            dp[i+1][0] = min(dp[i+1][0], dp[i][j] + n)
            dp[i+1][1] = min(dp[i+1][1], dp[i][j] + 10 - n)
    print(min(dp[l][0], dp[l][1]+1))
