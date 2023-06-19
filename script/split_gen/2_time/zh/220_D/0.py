def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(n):
            ndp = [0] * 10
            for k in range(10):
                ndp[(k + a[j]) % 10] += dp[k]
                ndp[(k + a[j]) % 10] %= mod
                ndp[(k * a[j]) % 10] += dp[k]
                ndp[(k * a[j]) % 10] %= mod
            dp = ndp
        ans[i] = dp[0]
    print(*ans, sep='\n')
