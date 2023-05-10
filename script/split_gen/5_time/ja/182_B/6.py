def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
ans = 0
max_gcd = 0
for i in range(2, 1001):
    gcd_cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            gcd_cnt += 1
    if gcd_cnt > max_gcd:
        max_gcd = gcd_cnt
        ans = i
print(ans)
