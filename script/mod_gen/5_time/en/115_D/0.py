def f(n, x):
    if n == 0:
        return 1
    elif x == 1:
        return 0
    elif x <= 1 + f(n - 1, x - 1):
        return f(n - 1, x - 1)
    elif x == 2 + f(n - 1, x - 2):
        return 1 + p[n - 1]
    elif x <= 2 + 2 * f(n - 1, x - 2):
        return 1 + p[n - 1] + f(n - 1, x - 2)
    else:
        return 1 + 2 * p[n - 1]
n, x = map(int, input().split())
p = [1]
for i in range(1, n + 1):
    p.append(2 * p[i - 1] + 1)
print(f(n, x))
