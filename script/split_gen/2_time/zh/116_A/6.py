def solve(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return solve(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + solve(n - 1, x - 2 - a[n - 1])
n, x = map(int, input().split())
p = [1]
a = [1]
for i in range(n):
    p.append(2 * p[i] + 1)
    a.append(2 * a[i] + 3)
print(solve(n, x))
