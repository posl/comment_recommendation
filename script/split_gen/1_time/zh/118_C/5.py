def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        r = a % b
        a, b = b, r
    return a
n = int(input())
a = list(map(int, input().split()))
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
print(g)
