def main():
    N, M = map(int, input().split())
    broken = set()
    for _ in range(M):
        broken.add(int(input()))
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    if 1 not in broken:
        dp[1] = 1
    for i in range(2, N+1):
        if i not in broken:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % 1000000007)

if __name__ == '__main__':
    main()