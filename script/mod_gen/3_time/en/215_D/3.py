def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = [i//2 for i in a]
lcm = 1
for i in range(n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
    if lcm > m:
        print(0)
        exit()
for i in range(n):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
print((m - lcm) // (lcm * 2) + 1)

if __name__ == '__main__':
    gcd()