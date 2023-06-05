def main():
    n, c = map(int, input().split())
    a = [0] * n
    b = [0] * n
    cost = [0] * n
    for i in range(n):
        a[i], b[i], cost[i] = map(int, input().split())
    max_day = max(b)
    dp = [0] * (max_day + 1)
    for i in range(n):
        dp[a[i] - 1] += cost[i]
        dp[b[i]] -= cost[i]
    for i in range(1, max_day + 1):
        dp[i] += dp[i - 1]
    print(min(c, min(dp)))

if __name__ == '__main__':
    main()