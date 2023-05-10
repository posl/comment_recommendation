def f(a,b):
    if a == 0:
        if b % 4 == 0:
            return b
        elif b % 4 == 1:
            return 1
        elif b % 4 == 2:
            return b + 1
        else:
            return 0
    else:
        return f(0, a-1) ^ f(0, b)
a, b = map(int, input().split())
print(f(a, b))
