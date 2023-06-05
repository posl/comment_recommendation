def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
l = [0]*n
r = [0]*n
l[0] = a[0]
r[-1] = a[-1]
for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])
for i in range(n-2, -1, -1):
    r[i] = gcd(r[i+1], a[i])
ans = max(l[-2], r[1])
for i in range(1, n-1):
    ans = max(ans, gcd(l[i-1], r[i+1]))
print(ans)

if __name__ == '__main__':
    gcd()