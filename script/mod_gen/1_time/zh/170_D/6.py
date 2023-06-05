def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
n = int(input())
a = list(map(int,input().split()))
a.sort()
b = [0]*n
c = [0]*n
for i in range(n):
    b[i] = a[i]
    c[i] = a[i]
for i in range(n-2,-1,-1):
    b[i] = gcd(b[i],b[i+1])
for i in range(1,n):
    c[i] = gcd(c[i],c[i-1])
ans = 1
for i in range(n):
    if i == 0:
        if a[i] % b[i+1] != 0:
            ans += 1
    elif i == n-1:
        if a[i] % c[i-1] != 0:
            ans += 1
    else:
        if gcd(b[i+1],c[i-1]) == 1:
            ans += 1
print(ans)

if __name__ == '__main__':
    gcd()