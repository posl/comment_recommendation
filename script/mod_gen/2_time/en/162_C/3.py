def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
K = int(input())
ans = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            ans += gcd(gcd(i, j), k)
print(ans)

if __name__ == '__main__':
    gcd()