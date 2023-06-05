def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    #dp[i][j]表示前i个数中选出j个数的方案数
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(N+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*i
    #ans[i]表示前i个数的方案数
    ans = [0 for _ in range(N+1)]
    for i in range(N+1):
        for j in range(i+1):
            ans[i] += dp[i][j]*pow(2, N-i, mod)
    res = 0
    for i in range(N):
        if A[i] == 1:
            res += ans[N-i]
            res %= mod
    print(res)
main()
