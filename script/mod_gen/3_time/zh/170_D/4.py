def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
a.sort()
b = [0] * n
for i in range(n):
    b[i] = gcd(b[i-1], a[i])
c = [0] * n
for i in range(n):
    c[i] = gcd(c[i-1], a[n-i-1])
ans = 0
for i in range(n):
    if i == 0:
        if c[n-i-2] % a[n-i-1] == 0:
            ans += 1
    elif i == n-1:
        if b[i-1] % a[i] == 0:
            ans += 1
    else:
        if b[i-1] % a[i] == 0 and c[n-i-2] % a[n-i-1] == 0:
            ans += 1
print(ans)

if __name__ == '__main__':
    gcd()