def f(n,k):
    if n%k==0:
        return 0
    else:
        return min(n%k,k-n%k)
n,k=map(int,input().split())
print(f(n,k))
