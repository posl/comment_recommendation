def main():
    n,k=map(int,input().split())
    l=[]
    r=[]
    for i in range(k):
        l1,r1=map(int,input().split())
        l.append(l1)
        r.append(r1)
    mod=998244353
    dp=[0 for i in range(n+1)]
    dp[1]=1
    for i in range(1,n+1):
        for j in range(k):
            if i-l[j]>0:
                dp[i]+=dp[i-l[j]]
                dp[i]%=mod
            if i-r[j]-1>=0:
                dp[i]-=dp[i-r[j]-1]
                dp[i]%=mod
    print(dp[n])
    
main()
