def func(a,b):
    if a==b:
        return 1
    elif a>b:
        return 0
    else:
        return sum([func(i,b) for i in range(a,b+1)])%998244353
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(sum([func(a[i],b[i]) for i in range(n)])%998244353)
