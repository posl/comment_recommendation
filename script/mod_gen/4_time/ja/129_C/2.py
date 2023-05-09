def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(1, 3):
            if i + j in A:
                continue
            if i + j > N:
                continue
            dp[i + j] += dp[i]
            dp[i + j] %= MOD
    print(dp[N])

if __name__ == '__main__':
    main()