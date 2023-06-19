def f(n,a,b):
    c=n//a
    d=n//b
    e=n//(a*b)
    return n*(n+1)//2 - (a+c)*c//2 - (b+d)*d//2 + (a*b+e)*e//2
n,a,b=map(int,input().split())
print(f(n,a,b))
