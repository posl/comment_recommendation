def f(a, b, x):
    if x <= a*a*b/2:
        return 90 - (x*2)/(a*b)
    else:
        return (a*a*b - x)*2/(a*a)
a, b, x = map(int, input().split())
print(f(a, b, x))
