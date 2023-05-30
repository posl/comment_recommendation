def solve():
    n, x = map(int, input().split())
    p = [1]
    for i in range(50):
        p.append(p[-1] * 2 + 1)
    def f(n, x):
        if n == 0:
            return 0 if x <= 0 else 1
        elif x <= 1 + p[n - 1]:
            return f(n - 1, x - 1)
        else:
            return p[n - 1] + 1 + f(n - 1, x - 2 - p[n - 1])
    return f(n, x)
print(solve())
