def main():
    X, Y = map(int, input().split())
    if X % 2 != Y % 2:
        print(0)
        return
    X, Y = (X + Y) // 2, (X - Y) // 2
    if X < 0 or Y < 0:
        print(0)
        return
    MOD = 10 ** 9 + 7
    dp = [0] * (X + 1)
    dp[0] = 1
    for i in range(Y + 1):
        for j in range(X, i - 1, -1):
            dp[j] = (dp[j] + dp[j - 1]) % MOD
    print(dp[X])
