def main():
    n,x,y = map(int,input().split())
    if x > y:
        x,y = y,x
    dp = [0]*(n+1)
    dp[2] = x
    for i in range(3,n+1):
        dp[i] = min(dp[i-1]+x,dp[i//2]+y+(i%2)*x)
    print(dp[n])
