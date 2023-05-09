def gcd(x,y):
    if x < y:
        x,y = y,x
    if x % y == 0:
        return y
    else:
        for i in range(y,0,-1):
            if x % i == 0 and y % i == 0:
                return i
a,b = map(int,input().split())
n = gcd(a,b)
ans = 1
