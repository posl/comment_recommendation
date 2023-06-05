def f(a, b):
    if a == b:
        return a
    else:
        return f(a, (a+b)//2) | f((a+b)//2+1, b)
a, b = map(int, input().split())
print(f(a, b))
