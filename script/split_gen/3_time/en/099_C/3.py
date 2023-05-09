def main():
    N = int(input())
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        for j in range(1, 7):
            if i - j**2 >= 0:
                dp[i] += dp[i-j**2]
    print(dp[N])
