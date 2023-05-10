def count_ways(n, m, broken):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i in broken:
            continue
        if i == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= MOD
    return dp[-1]
n, m = map(int, input().split())
broken = set([int(input()) for _ in range(m)])
print(count_ways(n, m, broken))

if __name__ == '__main__':
    count_ways()