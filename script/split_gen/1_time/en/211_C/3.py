def main():
    s = input()
    mod = 10**9 + 7
    dp = [0]*8
    for c in s:
        if c == "c":
            dp[0] += 1
        elif c == "h":
            dp[1] += dp[0]
        elif c == "o":
            dp[2] += dp[1]
        elif c == "k":
            dp[3] += dp[2]
        elif c == "u":
            dp[4] += dp[3]
        elif c == "d":
            dp[5] += dp[4]
        elif c == "a":
            dp[6] += dp[5]
        elif c == "i":
            dp[7] += dp[6]
    print(dp[7]%mod)
