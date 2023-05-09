def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(2, max(a)+1):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)
