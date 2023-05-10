def main():
    S = int(input())
    mod = 10**9 + 7
    dp = [0]*(S+1)
    dp[0] = 1
    for i in range(S+1):
        for j in range(i-2):
            dp[i] += dp[j]
            dp[i] %= mod
    print(dp[S])
