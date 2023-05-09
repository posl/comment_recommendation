def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
k = int(input())
ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans += gcd(gcd(a, b), c)
print(ans)

if __name__ == '__main__':
    gcd()