def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
b = []
for i in range(1,m+1):
    flag = True
    for j in range(n):
        if gcd(a[j],i) != 1:
            flag = False
            break
    if flag:
        b.append(i)
print(len(b))
for i in range(len(b)):
    print(b[i])
