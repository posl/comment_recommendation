def main():
    N,M = map(int,input().split())
    A = [0]*(N+1)
    for i in range(M):
        A[int(input())] = 1
    mod = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        if A[i] == 1:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2])%mod
    print(dp[N])
