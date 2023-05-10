def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
A, B = map(int, input().split())
C = gcd(A, B)
ans = 1
for i in range(2, int(C ** (1 / 2)) + 1):
    if C % i == 0:
        ans += 1
        if C // i != i:
            ans += 1
print(ans)
