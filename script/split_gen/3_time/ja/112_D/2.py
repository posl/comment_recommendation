def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = list(map(int, input().split()))
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
