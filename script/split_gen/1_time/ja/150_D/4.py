def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x // 2, a))
lcm = 1
for i in range(n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
for i in range(n):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
print((m // lcm + 1) // 2)
