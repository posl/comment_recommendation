def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x//2, a))
lcm = a[0]
for i in range(1, n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
lcm = lcm // 2
ans = m // lcm
print(ans)
