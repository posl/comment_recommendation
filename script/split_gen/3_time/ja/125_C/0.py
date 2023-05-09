def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x = y
        y = r
    return x
N = int(input())
A = [int(x) for x in input().split()]
A.sort()
ans = 0
for i in range(N):
    ans = gcd(ans, A[i])
print(ans)
