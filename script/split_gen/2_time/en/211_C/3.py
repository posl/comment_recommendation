def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [0] * 8
    for i in range(N):
        if S[i] == 'c':
            dp[0] += 1
        elif S[i] == 'h':
            dp[1] += dp[0]
        elif S[i] == 'o':
            dp[2] += dp[1]
        elif S[i] == 'k':
            dp[3] += dp[2]
        elif S[i] == 'u':
            dp[4] += dp[3]
        elif S[i] == 'd':
            dp[5] += dp[4]
        elif S[i] == 'a':
            dp[6] += dp[5]
        elif S[i] == 'i':
            dp[7] += dp[6]
        for j in range(8):
            dp[j] %= MOD
    print(dp[7])
