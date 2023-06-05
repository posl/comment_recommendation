def func(n,m,k):
    if n==1:
        if k<=m:
            return k
        else:
            return 0
    else:
        sum=0
        for i in range(1,m+1):
            sum+=func(n-1,m,k-i)
        return sum
n,m,k=map(int,input().split())
print(func(n,m,k)%998244353)
