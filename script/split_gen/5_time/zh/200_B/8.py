def f(n,k):
    for i in range(k):
        if n%200==0:
            n=n//200
        else:
            n=n*1000+200
    return n
n,k=map(int,input().split())
print(f(n,k))
