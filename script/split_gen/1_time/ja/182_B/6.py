def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(2,max(a)+1):
    cnt = 0
    for j in a:
        if j%i==0:
            cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)
