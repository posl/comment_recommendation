def main():
    N,M = map(int,input().split())
    A = [int(input()) for i in range(M)]
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    if 1 in A:
        dp[1] = 0
    else:
        dp[1] = 1
    for i in range(2,N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])
