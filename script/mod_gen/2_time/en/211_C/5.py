def main():
    S = input()
    S = S.replace("ch", "x")
    S = S.replace("o", "y")
    S = S.replace("k", "z")
    S = S.replace("u", "u")
    S = S.replace("d", "d")
    S = S.replace("a", "a")
    S = S.replace("i", "i")
    #print(S)
    MOD = 10**9 + 7
    dp = [0] * (len(S) + 1)
    dp[0] = 1
    for i in range(0, len(S)):
        if S[i] == "x":
            dp[i + 1] = dp[i + 1] + dp[i]
            dp[i + 1] = dp[i + 1] % MOD
        elif S[i] == "y":
            dp[i + 1] = dp[i + 1] + dp[i]
            dp[i + 1] = dp[i + 1] % MOD
        elif S[i] == "z":
            dp[i + 1] = dp[i + 1] + dp[i]
            dp[i + 1] = dp[i + 1] % MOD
        elif S[i] == "u":
            dp[i + 1] = dp[i + 1] + dp[i]
            dp[i + 1] = dp[i + 1] % MOD
        elif S[i] == "d":
            dp[i + 1] = dp[i + 1] + dp[i]
            dp[i + 1] = dp[i + 1] % MOD
        elif S[i] == "a":
            dp[i + 1] = dp[i + 1] + dp[i]
            dp[i + 1] = dp[i + 1] % MOD
        elif S[i] == "i":
            dp[i + 1] = dp[i + 1] + dp[i]
            dp[i + 1] = dp[i + 1] % MOD
        else:
            dp[i + 1] = 0
    print(dp[len(S)])

if __name__ == '__main__':
    main()