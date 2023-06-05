def f(h, n, a):
    a.sort()
    for i in range(n):
        h -= a[i]
        if h <= 0:
            return "Yes"
    return "No"
h, n = map(int, input().split())
a = list(map(int, input().split()))
print(f(h, n, a))
