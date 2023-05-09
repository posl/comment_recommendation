def swap(a, p, q, r, s):
    a[p-1:q], a[r-1:s] = a[r-1:s], a[p-1:q]
    return a
n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
b = swap(a, p, q, r, s)
print(*b)
