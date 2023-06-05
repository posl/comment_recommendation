def main():
    s = input()
    n = len(s)
    mod = 10**9+7
    dp = [[0]*8 for _ in range(n+1)]
    dp[n][0] = 1
    for i in range(n-1,-1,-1):
        for j in range(8):
            if s[i] == "?":
                for k in range(3):
                    dp[i][j] += dp[i+1][j*3+k]
            else:
                dp[i][j] += dp[i+1][j*3+ord(s[i])-ord("A")]
            dp[i][j] %= mod
    print(dp[0][0])
main()
