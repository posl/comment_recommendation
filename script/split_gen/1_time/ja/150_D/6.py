def lcm(x, y):
    return (x * y) // math.gcd(x, y)
n, m = map(int, input().split())
a = list(map(int, input().split()))
x = a[0] // 2
for i in range(1, n):
    x = lcm(x, a[i] // 2)
ans = m // x
print((ans + 1) // 2)
