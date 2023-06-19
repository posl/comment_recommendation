def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(10):
            dp = [0] * 10
            dp[(i + j) % 10] += 1
            for a in A:
                ndp = [0] * 10
                for k in range(10):
                    ndp[(k * a + (i + j)) % 10] += dp[k]
                    ndp[(k * a + (i * j)) % 10] += dp[k]
                dp = ndp
            for k in range(10):
                ans[k] += dp[k]
    for a in ans:
        print(a % MOD)
