def f(n,k,ls):
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        for j in range(k):
            if i-ls[j][0]>=0:
                dp[i]+=dp[i-ls[j][0]]
                dp[i]%=998244353
            if i-ls[j][1]-1>=0:
                dp[i]-=dp[i-ls[j][1]-1]
                dp[i]%=998244353
    return dp[n]
n,k=map(int,input().split())
ls=[]
for i in range(k):
    ls.append(list(map(int,input().split())))
print(f(n,k,ls))
