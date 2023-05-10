def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
l = []
r = []
for i in range(n):
    l.append(gcd(a[i], a[0]))
    r.append(gcd(a[i], a[n - 1]))
for i in range(n - 1):
    l[i + 1] = gcd(l[i], l[i + 1])
    r[n - i - 2] = gcd(r[n - i - 1], r[n - i - 2])
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, r[1])
    elif i == n - 1:
        ans = max(ans, l[n - 2])
    else:
        ans = max(ans, gcd(l[i - 1], r[i + 1]))
print(ans)

if __name__ == '__main__':
    gcd()