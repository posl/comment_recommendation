def main():
    #read
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10**9+7
    
    #solve
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        if i+1 not in A:
            dp[i+1] += dp[i]
        if i+2 not in A:
            dp[i+2] += dp[i]
        dp[i+1] %= MOD
        dp[i+2] %= MOD
    
    #print
    print(dp[N-1])
