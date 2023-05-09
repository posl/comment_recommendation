def f(a, b):
    if a == b:
        return a
    if a % 2 == 1 and b % 2 == 1:
        return 1
    if a % 2 == 0 and b % 2 == 0:
        return 0
    if a % 2 == 1 and b % 2 == 0:
        return f(a + 1, b)
    if a % 2 == 0 and b % 2 == 1:
        return f(a, b - 1) ^ b
a, b = map(int, input().split())
print(f(a, b))
