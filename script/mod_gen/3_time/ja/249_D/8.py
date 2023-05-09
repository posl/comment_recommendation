def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
a.sort()
a_max = a[-1]
a_min = a[0]
a_gcd = a[0]
for i in range(1, n):
    a_gcd = gcd(a_gcd, a[i])

if __name__ == '__main__':
    gcd()