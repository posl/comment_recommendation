def main():
    MOD = 10**9 + 7
    s = input()
    n = len(s)
    dp = [[[0] * 3 for _ in range(3)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(3):
            for k in range(3):
                if s[i] == "?":
                    for l in range(3):
                        dp[i + 1][j][k] += dp[i][j][k]
                        if j == 0 and k == 1:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 0 and k == 2:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 1 and k == 2:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 1 and k == 0:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 2 and k == 0:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 2 and k == 1:
                            dp[i + 1][j][k] += dp[i][j][k]
                        dp[i + 1][j][k] %= MOD
                else:
                    dp[i + 1][j][k] += dp[i][j][k]
                    if j == 0 and k == 1 and s[i] == "C":
                        dp[i + 1][j][k] += dp[i][j][k]
                    if j == 0 and k == 2 and s[i] == "B":
                        dp[i + 1][j][k] += dp[i][j][k]
                    if j == 1 and k == 2 and s[i] == "A":
                        dp[i + 1][j][k] += dp[i][j][k]
                    if j == 1 and k == 0 and s[i] == "C":
                        dp[i + 1][j][k] += dp[i][j][k]
                    if j == 2

if __name__ == '__main__':
    main()