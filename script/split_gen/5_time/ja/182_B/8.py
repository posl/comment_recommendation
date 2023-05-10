def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in a:
        if j % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)
