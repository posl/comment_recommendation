def swap(a, b, c, d, e):
    for i in range(b, c):
        a[i], a[i+d-b] = a[i+d-b], a[i]
    return a
n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
swap(a, p-1, q, r, s)
print(*a)
