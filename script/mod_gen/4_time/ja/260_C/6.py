def rec(n):
    if n==1:
        return 0
    if n in dp:
        return dp[n]
    dp[n]=rec(n-1)+X
    if n%2==0:
        dp[n]=min(dp[n],rec(n//2)+Y)
    else:
        dp[n]=min(dp[n],rec(n//2+1)+Y+X)
        dp[n]=min(dp[n],rec(n//2)+Y+X)
    return dp[n]
N,X,Y=map(int,input().split())
dp={}
print(rec(N))

if __name__ == '__main__':
    rec()