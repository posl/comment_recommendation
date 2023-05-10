def solution():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    dp = [0] * (N + 1)
    dp[1] = 1
    for a, b in AB:
        dp[b] += dp[a]
        dp[b] %= 1000000007
    print(dp[N])

if __name__ == '__main__':
    solution()