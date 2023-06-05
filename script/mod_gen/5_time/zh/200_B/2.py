def f(n,k):
    if k==0:
        return n
    if n%200==0:
        return f(n//200,k-1)
    else:
        return f(n*1000+200,k-1)
n,k=map(int,input().split())
print(f(n,k))
