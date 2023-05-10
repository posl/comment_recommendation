def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
n,x = map(int,input().split())
x_i = list(map(int,input().split()))
d = abs(x-x_i[0])
for i in range(1,n):
    d = gcd(d,abs(x-x_i[i]))
print(d)
