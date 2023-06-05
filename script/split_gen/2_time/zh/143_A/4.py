def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
A,B = map(int,input().split())
g = gcd(A,B)
cnt = 1
for i in range(2,int(g**0.5)+1):
    if g % i == 0:
        cnt += 1
        while g % i == 0:
            g //= i
