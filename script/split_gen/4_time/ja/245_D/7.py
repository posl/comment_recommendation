def calc(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    return c
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = [0] * m
for i in range(m):
    b[i] = (c[n + i] - calc(a, b)[n + i]) // a[n]
print(*b)
