def f(a, b):
    if a == b:
        return a
    if a == 0:
        return f(1, b)
    if a % 2 == 1:
        return f(a + 1, b) ^ a
    else:
        return f(a + 1, b)
a, b = map(int, input().split())
print(f(a, b))
