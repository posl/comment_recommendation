def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n
for i in range(1, n):
    l[i] = gcd(l[i - 1], a[i - 1])
    r[n - i - 1] = gcd(r[n - i], a[n - i])
ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i]))
print(ans)
