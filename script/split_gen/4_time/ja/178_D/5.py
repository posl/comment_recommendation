def main():
    s = int(input())
    dp = [0]*(s+1)
    dp[0] = 1
    for i in range(3,s+1):
        for j in range(s-i+1):
            dp[j+i] += dp[j]
            dp[j+i] %= 10**9+7
    print(dp[s])
