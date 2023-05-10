def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #compute
    MOD = 998244353
    dp = [0]*10
    dp[A[0]] = 1
    for i in range(1, N):
        dp2 = [0]*10
        for j in range(10):
            dp2[(j+A[i])%10] += dp[j]
            dp2[(j*A[i])%10] += dp[j]
        for j in range(10):
            dp[j] = dp2[j] % MOD
    #output
    print(*dp, sep='\n')
