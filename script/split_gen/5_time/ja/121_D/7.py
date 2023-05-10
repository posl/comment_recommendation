def func(a, b):
    if a == b:
        return a
    elif a == 0:
        return func(a+1, b)
    elif a % 2 == 0:
        return func(a+1, b) ^ a
    else:
        return func(a-1, b) ^ a
a, b = map(int, input().split())
print(func(a, b))
