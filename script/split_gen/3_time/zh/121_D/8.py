def f(a, b):
    if a == b:
        return a
    if a % 2 == 0 and b % 2 == 0:
        return f(a // 2, b // 2) * 2
    if a % 2 == 0 and b % 2 == 1:
        return f(a // 2, b // 2) * 2 + 1
    if a % 2 == 1 and b % 2 == 0:
        return f((a + 1) // 2, b // 2) * 2
    if a % 2 == 1 and b % 2 == 1:
        return f((a + 1) // 2, b // 2) * 2 + 1
a, b = map(int, input().split())
print(f(a, b))
