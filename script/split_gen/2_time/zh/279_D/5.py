def f(x):
    return A * x + (B / (x ** 0.5))
A, B = map(int, input().split())
l, r = 0, 10 ** 9
for _ in range(100):
    c1 = (2 * l + r) / 3
    c2 = (l + 2 * r) / 3
    if f(c1) < f(c2):
        r = c2
    else:
        l = c1
print(f(l))
