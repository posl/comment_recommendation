def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            d = gcd(a, b)
            ans += gcd(c, d)
print(ans)

if __name__ == '__main__':
    gcd()