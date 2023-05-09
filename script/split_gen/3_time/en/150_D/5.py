def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
g = a[0]
for i in range(n):
    g = gcd(g, a[i])
for i in range(n):
    if (a[i] // 2) % g == 0:
        print(0)
        exit()
print((m // g + 1) // 2)
