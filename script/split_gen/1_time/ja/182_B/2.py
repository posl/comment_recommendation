def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(2, max(a)+1):
    cnt = 0
    for j in range(n):
        if a[j]%i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)
