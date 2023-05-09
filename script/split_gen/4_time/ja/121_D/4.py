def f(a,b):
    if a == b:
        return a
    elif a == 0:
        return f(b)
    else:
        return f(b) ^ f(a-1)
a,b = map(int,input().split())
print(f(a,b))
