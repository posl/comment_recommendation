def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
lcm = 1
for i in range(n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
print(lcm)
