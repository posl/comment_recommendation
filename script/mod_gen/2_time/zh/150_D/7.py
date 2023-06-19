def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
lcm = a[0]
for i in range(1, n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
for i in range(n):
    if lcm // a[i] % 2 == 0:
        print(0)
        exit()
m //= lcm
ans = (m + 1) // 2
print(ans)

if __name__ == '__main__':
    gcd()