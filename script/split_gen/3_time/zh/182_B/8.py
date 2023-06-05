def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x%y)
n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(2, 1001):
    tmp = 0
    for j in range(n):
        if a[j]%i == 0:
            tmp += 1
    if tmp >= cnt:
        ans = i
        cnt = tmp
print(ans)
