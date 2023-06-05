def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
b = [0] * n
c = [0] * n
b[0] = a[0]
c[n-1] = a[n-1]
for i in range(1,n):
    b[i] = gcd(b[i-1], a[i])
    c[n-i-1] = gcd(c[n-i], a[n-i-1])
ans = 0
for i in range(n):
    if i == 0:
        if c[i+1] % a[i] != 0:
            ans += 1
    elif i == n-1:
        if b[i-1] % a[i] != 0:
            ans += 1
    else:
        if gcd(b[i-1], c[i+1]) % a[i] != 0:
            ans += 1
print(ans)

if __name__ == '__main__':
    gcd()