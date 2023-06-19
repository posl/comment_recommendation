def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
n,m = map(int,input().split())
for i in range(int(m/n),0,-1):
    if m%i == 0:
        if gcd(i,m//i) == 1:
            print(i)
            break
