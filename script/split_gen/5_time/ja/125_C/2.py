def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
l = [0] * (n + 1)
r = [0] * (n + 1)
for i in range(n):
    l[i + 1] = gcd(l[i], a[i])
for i in range(n - 1, -1, -1):
    r[i] = gcd(r[i + 1], a[i])
ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i + 1]))
print(ans)
