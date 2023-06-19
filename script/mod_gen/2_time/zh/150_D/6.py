def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lcm = a[0]
for i in range(1, n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
count = 0
for i in range(n):
    count += (lcm // a[i]) // 2
print(count % (10 ** 9 + 7))

if __name__ == '__main__':
    gcd()