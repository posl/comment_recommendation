def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
max_gcd = 0
for i in range(2, a[0]+1):
    cnt = 0
    for j in a:
        if j % i == 0:
            cnt += 1
    if cnt > max_gcd:
        ans = i
        max_gcd = cnt
print(ans)
