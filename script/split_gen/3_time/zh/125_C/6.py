def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, n):
    ans = gcd(ans, a[i])
print(ans)
