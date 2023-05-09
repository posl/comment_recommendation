def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [0]*(B[0]+1)
    for i in range(A[0], B[0]+1):
        dp[i] = 1
    for i in range(1, N):
        for j in range(B[i]+1):
            dp[j] = dp[j] + dp[j-1]
            dp[j] %= MOD
        for j in range(A[i], B[i]+1):
            dp[j] += dp[j-1]
            dp[j] %= MOD
    print(dp[B[-1]])
solve()

if __name__ == '__main__':
    solve()