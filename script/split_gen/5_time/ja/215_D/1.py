def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n,m = map(int,input().split())
a = list(map(int,input().split()))
x = [0]*(m+1)
for i in range(n):
    for j in range(1,m+1):
        if gcd(a[i],j) == 1:
            x[j] = 1
print(sum(x))
for i in range(m+1):
    if x[i] == 1:
        print(i)
