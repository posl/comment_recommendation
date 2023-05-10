def main():
    N, M = map(int, input().split())
    broken_steps = set()
    for i in range(M):
        broken_steps.add(int(input()))
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in broken_steps:
            continue
        if i - 1 not in broken_steps:
            dp[i] += dp[i - 1]
        if i - 2 not in broken_steps:
            dp[i] += dp[i - 2]
        dp[i] %= 1000000007
    print(dp[N])

if __name__ == '__main__':
    main()