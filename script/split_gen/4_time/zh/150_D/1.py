def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()
lcm = a[0]
for i in range(1, len(a)):
    lcm = lcm * a[i] // gcd(lcm, a[i])
for i in range(len(a)):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
ans = m // lcm
ans = (ans + 1) // 2
print(ans)
