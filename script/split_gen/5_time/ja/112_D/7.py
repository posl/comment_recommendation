def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
lcm = 1
for i in range(n):
    a[i] //= 2
    lcm *= a[i] // gcd(lcm, a[i])
for i in range(n):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
print((m // lcm + 1) // 2)
