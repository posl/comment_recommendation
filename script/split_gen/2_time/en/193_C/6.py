def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n-1])
