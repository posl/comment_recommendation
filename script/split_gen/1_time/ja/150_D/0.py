def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x // 2, a))
lcm = 1
for i in a:
    lcm = lcm * i // gcd(lcm, i)
for i in a:
    if (lcm // i) % 2 == 0:
        print(0)
        exit()
m = m // lcm
ans = (m + 1) // 2
print(ans)
