def f(a,b):
    if a==b:
        return a
    else:
        return f(a//2,b//2)*2
a,b=map(int,input().split())
print(f(a,b))
