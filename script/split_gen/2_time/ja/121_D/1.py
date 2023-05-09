def f(a, b):
    if a == b:
        return a
    if a % 2 == 0:
        if b % 2 == 0:
            return b ^ f(a, b - 1)
        else:
            return f(a, b - 1)
    else:
        if b % 2 == 0:
            return f(a + 1, b) ^ a
        else:
            return a ^ f(a + 1, b)
a, b = map(int, input().split())
print(f(a, b))
