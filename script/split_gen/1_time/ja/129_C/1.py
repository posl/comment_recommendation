def main():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    for _ in range(m):
        a[int(input())] = 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if a[i] == 0:
            dp[i + 1] += dp[i]
            dp[i + 1] %= 1000000007
            if i + 2 <= n:
                dp[i + 2] += dp[i]
                dp[i + 2] %= 1000000007
    print(dp[n])
