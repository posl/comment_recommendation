def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
g = gcd(a, b)
a //= g
b //= g
ans = pow(2, n, mod) - 1
c1 = c2 = 1
for i in range(b):
    c1 = c1 * (n - i) * pow(i + 1, mod - 2, mod) % mod
for i in range(a):
    c2 = c2 * (n - i) * pow(i + 1, mod - 2, mod) % mod
ans = (ans - c1 - c2) % mod
print(ans)
