def main():
    L = int(input())
    dp = [0] * (L+1)
    dp[0] = 1
    for i in range(1, L+1):
        for j in range(0, i):
            dp[i] += dp[j] * dp[i-1-j]
    print(dp[L])
