def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
K = int(input())
ans = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            ans += gcd(i, gcd(j, k))
print(ans)
