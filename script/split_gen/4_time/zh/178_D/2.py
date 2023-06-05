def main():
    S = int(input())
    mod = 1000000007
    dp = [0 for i in range(S+1)]
    dp[0] = 1
    for i in range(3, S+1):
        for j in range(S-i+1):
            dp[i+j] += dp[j]
            dp[i+j] %= mod
    print(dp[-1])
