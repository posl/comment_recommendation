def f(a, b):
    if a == b:
        return a
    if a == 0:
        return f(0, b)
    if a & 1:
        return f(a + 1, b) ^ a
    if b & 1:
        return f(a, b - 1) ^ b
    return f(a >> 1, b >> 1) << 1
a, b = map(int, input().split())
print(f(a, b))
