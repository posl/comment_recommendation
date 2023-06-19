def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
a = [int(x) for x in input().split()]
l = [0] * n
r = [0] * n
l[0] = a[0]
r[n-1] = a[n-1]
for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])
for i in range(n-2, -1, -1):
    r[i] = gcd(r[i+1], a[i])
max_gcd = 0
for i in range(0, n):
    if i == 0:
        max_gcd = max(max_gcd, r[i+1])
    elif i == n-1:
        max_gcd = max(max_gcd, l[i-1])
    else:
        max_gcd = max(max_gcd, gcd(l[i-1], r[i+1]))
print(max_gcd)
