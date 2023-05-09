def main():
    L = int(input())
    dp = [0 for _ in range(L+1)]
    dp[0] = 1
    for i in range(0, L+1):
        for j in range(0, i):
            dp[i] += dp[j] * dp[i-j-1]
    print(dp[L])
