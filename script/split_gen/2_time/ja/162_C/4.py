def gcd(a, b, c):
    ret = 1
    for i in range(2, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            ret = i
    return ret
K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            ans += gcd(a, b, c)
print(ans)
