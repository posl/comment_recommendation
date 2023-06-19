def f(a,b):
    if a==b:
        return a
    elif a+1==b:
        return a^b
    else:
        return f(a,b-1)^b
a,b = map(int,input().split())
print(f(a,b))
