def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a
n = int(input())
a = list(map(int, input().split()))
l = [0] * (n+1)
r = [0] * (n+1)
for i in range(n):
    l[i+1] = gcd(l[i], a[i])
    r[n-1-i] = gcd(r[n-i], a[n-1-i])
ans = 1
for i in range(n):
    ans = max(ans, gcd(l[i], r[i+1]))
print(ans)
