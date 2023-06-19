def main():
    S = input()
    l = len(S)
    dp = [[0 for _ in range(2)] for _ in range(l+1)]
    dp[0][0] = 0
    dp[0][1] = 1
    for i in range(l):
        dp[i+1][0] = min(dp[i][0] + int(S[i]), dp[i][1] + (10 - int(S[i])))
        dp[i+1][1] = min(dp[i][0] + int(S[i]) + 1, dp[i][1] + (10 - int(S[i]) - 1))
    print(dp[l][0])

if __name__ == '__main__':
    main()