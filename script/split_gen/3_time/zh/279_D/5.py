def f(x):
    return x + a / (b + x**0.5)
a, b = map(int,input().split())
l = 0
r = 1e18
for i in range(1000):
    c1 = (l * 2 + r) / 3
    c2 = (l + r * 2) / 3
    if f(c1) < f(c2):
        r = c2
    else:
        l = c1
print(f(l))
