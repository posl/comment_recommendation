def f(n,m,k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    if dp[n][k] != -1:
        return dp[n][k]
    res = 0
    for i in range(m+1):
        if k-i >= 0:
            res += f(n-1,m,k-i)
    dp[n][k] = res % 998244353
    return dp[n][k]
N,M,K = map(int,input().split())
dp = [[-1 for i in range(K+1)] for j in range(N+1)]
print(f(N,M,K))
