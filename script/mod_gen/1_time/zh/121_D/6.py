def f(a, b):
    if a == b:
        return a
    elif a == b - 1:
        return a ^ b
    elif a % 2 == 0 and b % 2 == 0:
        return f(a >> 1, b >> 1) << 1
    elif a % 2 == 0 and b % 2 == 1:
        return (f(a >> 1, b >> 1) << 1) + 1
    elif a % 2 == 1 and b % 2 == 0:
        return (f(a >> 1, b >> 1) << 1) + 1
    else:
        return (f(a >> 1, b >> 1) << 1) + 2
a, b = map(int, input().split())
print(f(a, b))
