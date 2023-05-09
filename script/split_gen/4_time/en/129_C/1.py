def main():
    n, m = map(int, input().split())
    broken = [False] * (n + 1)
    for _ in range(m):
        broken[int(input())] = True
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if broken[i + 1]:
            continue
        dp[i + 1] += dp[i]
        dp[i + 1] %= 1000000007
        if i + 2 <= n:
            dp[i + 2] += dp[i]
            dp[i + 2] %= 1000000007
    print(dp[n])
