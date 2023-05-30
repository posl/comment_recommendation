def f(n,k):
    if k%2==0:
        return (n//k)**3 + (n//(k//2)-n//k)**3
    else:
        return (n//k)**3
n,k=map(int,input().split())
print(f(n,k))
