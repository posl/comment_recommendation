def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int,input().split()))
l = [0] * (10**6+1)
for i in range(n):
    l[a[i]] += 1
ans = 0
for i in range(2,10**6+1):
    cnt = 0
    for j in range(i,10**6+1,i):
        cnt += l[j]
    if cnt == 1:
        ans += 1
print(ans)
