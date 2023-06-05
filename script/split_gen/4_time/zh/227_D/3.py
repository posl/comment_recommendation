def f(n,k,a):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    ans=0
    for i in d:
        if d[i]>=k:
            ans+=k
        else:
            ans+=d[i]
    return ans
n,k=map(int,input().split())
a=list(map(int,input().split()))
print(f(n,k,a))
