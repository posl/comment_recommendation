def f(a, b):
    if a == b:
        return a
    else:
        return a ^ f(a+1, b)
a, b = map(int, input().split())
print(f(a, b))
