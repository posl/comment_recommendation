def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(N):
            ndp = [0] * 10
            for k in range(10):
                ndp[(k + A[j]) % 10] = (ndp[(k + A[j]) % 10] + dp[k]) % MOD
                ndp[(k * A[j]) % 10] = (ndp[(k * A[j]) % 10] + dp[k]) % MOD
            dp = ndp
        ans[i] = dp[0]
    print(*ans, sep="\n")

if __name__ == '__main__':
    main()