def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N)
    MOD = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= MOD
    print(dp[N])

if __name__ == '__main__':
    main()