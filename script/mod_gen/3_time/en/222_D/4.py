def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1] += dp[i]
            dp[i + 1] %= MOD
    print(dp[N])

if __name__ == '__main__':
    main()