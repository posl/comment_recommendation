def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
K = int(input())
ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            ans += gcd(a, gcd(b, c))
print(ans)

if __name__ == '__main__':
    gcd()