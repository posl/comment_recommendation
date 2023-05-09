def main():
    s = input()
    MOD = 10 ** 9 + 7
    n = len(s)
    dp = [0] * 3
    dp[0] = 1
    for i in range(n):
        if s[i] == "A":
            dp[0] += dp[0]
        elif s[i] == "B":
            dp[1] += dp[0]
        elif s[i] == "C":
            dp[2] += dp[1]
        else:
            dp[2] += 3 * dp[2] + dp[1]
            dp[1] += 3 * dp[1] + dp[0]
            dp[0] += 3 * dp[0]
        dp[0] %= MOD
        dp[1] %= MOD
        dp[2] %= MOD
    print(dp[2])
