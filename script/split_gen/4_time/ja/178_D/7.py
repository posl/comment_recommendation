def main():
    s = int(input())
    if s == 1 or s == 2:
        print(0)
    else:
        dp = [0] * (s+1)
        dp[0] = 1
        for i in range(3, s+1):
            for j in range(0, i-2):
                dp[i] += dp[j]
                dp[i] %= 1000000007
        print(dp[s])
