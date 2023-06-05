def climb(N,M,a):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        dp = [0 for i in range(N+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,N+1):
            if i in a:
                dp[i] = 0
            else:
                dp[i] = dp[i-1] + dp[i-2]
    return dp[N]
N,M = map(int,input().split())
a = []
for i in range(M):
    a.append(int(input()))
print(climb(N,M,a)%1000000007)
