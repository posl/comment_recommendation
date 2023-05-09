def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = [0] * (m + 1)
for i in range(n):
    for j in range(1, m // a[i] + 1):
        b[a[i] * j] += 1
c = []
for i in range(1, m + 1):
    if b[i] == 0:
        c.append(i)
print(len(c))
for i in range(len(c)):
    print(c[i])
