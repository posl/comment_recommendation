def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
k = int(input())
ans = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            ans += gcd(i,gcd(j,l))
print(ans)
