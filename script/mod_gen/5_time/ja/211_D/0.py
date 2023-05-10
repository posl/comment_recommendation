def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    mod = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for a, b in AB:
            if b == i:
                dp[i] += dp[a]
                dp[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()