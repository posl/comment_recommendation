def func(a,b,k):
    c=a*b
    d=c//a
    e=c//b
    f=d+e
    g=f//2
    h=g//k
    return h
a,b,k=map(int,input().split())
print(func(a,b,k))
