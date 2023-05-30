def f(a, b):
    if a == b:
        return a
    if a % 2 == 0:
        if (b - a) % 2 == 0:
            return (b - a) ^ b
        else:
            return (b - a) ^ b ^ 1
    else:
        if (b - a) % 2 == 0:
            return (b - a) ^ b ^ a
        else:
            return (b - a) ^ b ^ a ^ 1
a, b = map(int, input().split())
print(f(a, b))
