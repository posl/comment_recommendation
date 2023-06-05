def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    while b > 0:
        a, b = b, a % b
    return a
n = int(input())
a = list(map(int, input().split()))
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
l[0] = a[0]
r[n - 1] = a[n - 1]
for i in range(1, n):
    l[i] = gcd(l[i - 1], a[i])
    r[n - i - 1] = gcd(r[n - i], a[n - i - 1])
ans = max(l[n - 2], r[1])
for i in range(1, n - 1):
    ans = max(ans, gcd(l[i - 1], r[i + 1]))
print(ans)
