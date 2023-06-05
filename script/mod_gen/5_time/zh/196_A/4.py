def f(a, b, c, d):
    return max(a * c, a * d, b * c, b * d)
a, b = map(int, input().split())
c, d = map(int, input().split())
print(f(a, b, c, d))
