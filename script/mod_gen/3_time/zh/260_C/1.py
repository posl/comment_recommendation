def f(n,x,y):
    if n==1:
        return 0
    elif n==2:
        return x
    else:
        return f(n-1,x,y)+f(n-2,x,y)+x
n,x,y=map(int,input().split())
print(f(n,x,y))
