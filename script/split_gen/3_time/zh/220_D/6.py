def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    def f(x, y):
        return (x + y) % 10
    def g(x, y):
        return (x * y) % 10
    for i in range(10):
        for j in range(10):
            for k in range(10):
                dp = [0] * 10
                dp[f(f(i, j), k)] = 1
                dp[f(g(i, j), k)] = 1
                dp[g(f(i, j), k)] = 1
                dp[g(g(i, j), k)] = 1
                for a in range(10):
                    ans[a] += dp[a] * A.count(i) * A.count(j) * A.count(k)
                    ans[a] %= MOD
    for i in range(10):
        print(ans[i])
solve()
