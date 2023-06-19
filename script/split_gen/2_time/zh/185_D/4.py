def solve(n, m, a):
    a.sort()
    if m == 0:
        return 1
    if m == n:
        return 0
    if m == 1:
        return n - 1
    d = []
    for i in range(m - 1):
        d.append(a[i + 1] - a[i] - 1)
    d.sort()
    return n - 1 - sum(d[-(m - 1):])
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
