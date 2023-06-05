def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lcm = a[0]
for i in range(1, n):
    lcm = a[i] * lcm // gcd(a[i], lcm)
for i in range(n):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
lcm //= 2
ans = m // lcm
print((ans + 1) // 2)
