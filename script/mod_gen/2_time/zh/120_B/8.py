def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a, b, k = map(int, input().split())
c = gcd(a, b)
ans = 1
for i in range(c, 0, -1):
    if c % i == 0:
        k -= 1
        if k == 0:
            ans = i
            break
print(ans)

if __name__ == '__main__':
    gcd()