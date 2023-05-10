def main():
    N, M = map(int, input().split())
    broken = set()
    for i in range(M):
        broken.add(int(input()))
    mod = 1000000007
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in broken:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()