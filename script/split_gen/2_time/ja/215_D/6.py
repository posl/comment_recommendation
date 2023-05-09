def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
n,m = map(int,input().split())
a = list(map(int,input().split()))
l = [0]*(m+1)
for i in range(n):
    for j in range(1,m+1):
        if gcd(a[i],j) == 1:
            l[j] += 1
ans = []
for i in range(1,m+1):
    if l[i] == n:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
