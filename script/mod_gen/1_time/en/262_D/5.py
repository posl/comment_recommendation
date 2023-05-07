def main():
    MOD = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0 for _ in range(N + 1)]
    dp[0] = 1
    for i in range(N):
        for j in range(N - 1, -1, -1):
            dp[j + 1] = (dp[j + 1] + dp[j]) % MOD
    ans = 0
    for i in range(1, N + 1):
        ans += (dp[i] * A[i - 1] * pow(i, MOD - 2, MOD)) % MOD
    print(ans % MOD)

if __name__ == '__main__':
    main()