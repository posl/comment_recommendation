def main():
    N, M = map(int, input().split())
    broken = set()
    for _ in range(M):
        broken.add(int(input()))
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i not in broken:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= 10 ** 9 + 7
    print(dp[-1])

if __name__ == '__main__':
    main()