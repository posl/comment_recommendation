def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
a, b = map(int, input().split())
gcd_ab = gcd(a, b)
ans = 1
for i in range(2, int(gcd_ab**0.5)+1):
    if gcd_ab % i == 0:
        ans += 1
        while gcd_ab % i == 0:
            gcd_ab //= i
