def f(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)
r, D, x = map(int, input().split())
f(r, D, x)
