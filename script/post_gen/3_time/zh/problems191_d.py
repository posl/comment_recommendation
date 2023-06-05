Synthesizing 9/10 solutions

=======
Suggestion 1

def solve(x, y, r):
    # Write your code here
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    # Write your code here
    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    ans = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                ans += 1
    print(ans)

=======
Suggestion 2

def count(x,y,r):
    count = 0
    for i in range(int(x-r),int(x+r)+1):
        for j in range(int(y-r),int(y+r)+1):
            if (x-i)**2 + (y-j)**2 <= r**2:
                count += 1
    return count

x,y,r = map(float,input().split())
print(count(x,y,r))

=======
Suggestion 3

def solve(x, y, r):
    x1 = int(x*10000)
    y1 = int(y*10000)
    r1 = int(r*10000)
    ans = 0
    for i in range(x1-r1, x1+r1+1):
        for j in range(y1-r1, y1+r1+1):
            if (i-x1)*(i-x1) + (j-y1)*(j-y1) <= r1*r1:
                ans += 1
    return ans

=======
Suggestion 4

def grid_in_circle(x, y, r):
    x1 = int(x - r)
    x2 = int(x + r)
    y1 = int(y - r)
    y2 = int(y + r)
    count = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                count += 1
    return count

=======
Suggestion 5

def main():
    x,y,r = map(float, input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    count = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if (i-x)*(i-x)+(j-y)*(j-y) <= r*r:
                count += 1
    print(count)

=======
Suggestion 6

def count_points_in_circle(x, y, r):
    import math
    import decimal
    decimal.getcontext().prec = 30
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP
    x = decimal.Decimal(x)
    y = decimal.Decimal(y)
    r = decimal.Decimal(r)
    x_min = math.floor(x - r)
    x_max = math.ceil(x + r)
    y_min = math.floor(y - r)
    y_max = math.ceil(y + r)
    count = 0
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if (x - i)**2 + (y - j)**2 <= r**2:
                count += 1
    return count

=======
Suggestion 7

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    X,Y,R=map(float,input().split())
    X,Y,R=int(X*10000),int(Y*10000),int(R*10000)
    X1,X2=X-R,X+R
    Y1,Y2=Y-R,Y+R
    ans=0
    for x in range(X1,X2+1):
        for y in range(Y1,Y2+1):
            if (x-X)*(x-X)+(y-Y)*(y-Y)<=R*R:
                ans+=1
    print(ans)
