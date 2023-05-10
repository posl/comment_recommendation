def swap(a, p, q, r, s):
    b = a.copy()
    for i in range(p-1, q):
        b[r-1+i-(q-p)] = a[i]
    for i in range(r-1, s):
        b[p-1+i-(r-q)] = a[i]
    return b
n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
b = swap(a, p, q, r, s)
print(*b)
