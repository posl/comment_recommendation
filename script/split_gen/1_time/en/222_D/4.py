def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [0] * (3001)
    dp[0] = 1
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[j] = (dp[j] + dp[j-1]) % MOD
    print(dp[B[-1]])
