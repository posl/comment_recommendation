def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a
n,m = map(int,input().split())
a = list(map(int,input().split()))
a = list(set(a))
a.sort()
ans = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]*a[j] > 2*m:
            break
        if gcd(a[i],a[j]) == a[i]:
            ans += 1
print(ans)
