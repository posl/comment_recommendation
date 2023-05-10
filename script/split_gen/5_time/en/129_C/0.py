def main():
    N, M = map(int, input().split())
    broken = set([int(input()) for _ in range(M)])
    dp = [0] * (N + 1)
    dp[0] = 1
    if 1 not in broken:
        dp[1] = 1
    for i in range(2, N + 1):
        if i not in broken:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= 1000000007
    print(dp[N])
