def gcd(a,b):
    while b:
        a,b = b, a % b
    return a
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
cnt = 0
for i in range(2,a[-1]+1):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if tmp > cnt:
        cnt = tmp
        ans = i
print(ans)
