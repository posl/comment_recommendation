def f(a, b):
    return a ^ b ^ (a + 1) ^ (b + 1) if (b - a) % 2 else 0
a, b = map(int, input().split())
print(f(a, b))
