def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n
l[0] = a[0]
r[-1] = a[-1]
for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])
    r[n-i-1] = gcd(r[n-i], a[n-i-1])
ans = max(l[n-2], r[1])
for i in range(1, n-1):
    ans = max(ans, gcd(l[i-1], r[i+1]))
print(ans)
