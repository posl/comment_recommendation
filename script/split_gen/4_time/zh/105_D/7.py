def solve(n,m,a):
    sum=0
    for i in range(n):
        sum+=a[i]
    if sum%m==0:
        sum=sum//m
    else:
        sum=sum//m+1
    a.append(0)
    sum=sum%m
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(n):
        dp[i+1]=dp[i]+a[i]
    dp.sort()
    ans=0
    for i in range(n):
        if dp[i+1]-dp[i]>=sum:
            ans+=dp[i+1]-dp[i]-sum
        else:
            ans+=m-(sum-dp[i+1]+dp[i])
    return ans
