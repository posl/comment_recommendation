def growth(r, D, x):
    return r * x - D
r, D, x = map(int, input().split())
for i in range(10):
    x = growth(r, D, x)
    print(x)
