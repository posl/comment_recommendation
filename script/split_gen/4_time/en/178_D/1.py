def main():
    S = int(input())
    MOD = 10**9 + 7
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(3, S + 1):
        dp[i] = dp[i - 3] + dp[i - 1]
        dp[i] %= MOD
    print(dp[S])
