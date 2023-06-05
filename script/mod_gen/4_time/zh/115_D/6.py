def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return f(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + f(n - 1, x - 2 - a[n - 1])
n, x = map(int, input().split())
a = [1]
p = [1]
for i in range(n):
    a.append(3 + 2 * a[i])
    p.append(1 + 2 * p[i])
print(f(n, x))
