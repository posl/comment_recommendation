Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, r = map(float, input().split())
    x = int(x * 1000)
    y = int(y * 1000)
    r = int(r * 1000)
    ans = 0
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            if i * i + j * j <= r * r:
                if x + i >= 0 and x + i <= 100000 and y + j >= 0 and y + j <= 100000:
                    ans += 1
    print(ans)
    return

=======
Suggestion 2

def main():
    X, Y, R = map(float, input().split())
    X = int(X*10)
    Y = int(Y*10)
    R = int(R*10)
    ans = 0
    for x in range(X-R, X+R+1):
        d = R**2 - (x-X)**2
        if d < 0:
            continue
        y1 = Y - int(d**0.5)
        y2 = Y + int(d**0.5)
        ans += y2-y1+1
    print(ans)

main()

=======
Suggestion 3

def main():
    x, y, r = map(float, input().split())
    # x, y, r = map(float, "0.2 0.8 1.1".split())
    # x, y, r = map(float, "100 100 1".split())
    # x, y, r = map(float, "42782.4720 31949.0192 99999.99".split())
    # print(x, y, r)

    # r = int(r)
    r = int(r) + 1

    # x = int(x)
    # y = int(y)
    x = int(x + 0.5)
    y = int(y + 0.5)

    print(x, y, r)

    count = 0
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                count += 1

    print(count)

=======
Suggestion 4

def main():
    X, Y, R = map(float, input().split())
    import math
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        if x < 0 or x > 10**5 * 10000:
            continue
        y = int(math.sqrt(R**2 - (x - X)**2)) + Y
        if y < 0 or y > 10**5 * 10000:
            continue
        ans += 1
    for x in range(X - R, X + R + 1):
        if x < 0 or x > 10**5 * 10000:
            continue
        y = -int(math.sqrt(R**2 - (x - X)**2)) + Y
        if y < 0 or y > 10**5 * 10000:
            continue
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    X, Y, R = map(float, input().split())
    X, Y = int(X*100), int(Y*100)
    R = int(R*100)
    ans = 0
    for x in range(-R, R+1):
        if x*X < 0: continue
        y = int((R**2 - x**2)**0.5)
        if y*Y < 0: continue
        ans += y*2 + 1
    print(ans)

=======
Suggestion 6

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 1000)
    Y = int(Y * 1000)
    R = int(R * 1000)
    X2 = X * X
    Y2 = Y * Y
    R2 = R * R
    x0 = X - R
    x1 = X + R
    y0 = Y - R
    y1 = Y + R
    x0 = x0 // 1000
    x1 = x1 // 1000
    y0 = y0 // 1000
    y1 = y1 // 1000
    ans = 0
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            x2 = x * x
            y2 = y * y
            if (x2 + y2 + X2 + Y2 - 2 * x * X - 2 * y * Y) <= R2:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    x,y,r = map(float,input().split())
    #print(x,y,r)
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    #print(x,y,r)
    count = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if i**2 + j**2 <= r**2:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    x, y, r = map(float, input().split())
    r = int(r)
    #print(x, y, r)
    count = 0
    for i in range(r+1):
        for j in range(r+1):
            #print(i, j)
            if i**2 + j**2 <= r**2:
                count += 1
    print(count*4)

=======
Suggestion 9

def main():
    from sys import stdin
    # from math import ceil
    # from math import floor
    # from decimal import Decimal
    # from decimal import ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_HALF_DOWN
    f_i = stdin
    
    X, Y, R = [float(x) for x in f_i.readline().split()]
    
    # R = Decimal(R)
    # X = Decimal(X)
    # Y = Decimal(Y)
    # R = R.quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
    # X = X.quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
    # Y = Y.quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
    # R = float(R)
    # X = float(X)
    # Y = float(Y)
    R = round(R, 4)
    X = round(X, 4)
    Y = round(Y, 4)
    
    # print(R)
    # print(X)
    # print(Y)
    
    # print(ceil(X+R))
    # print(ceil(Y+R))
    # print(floor(X-R))
    # print(floor(Y-R))
    
    count = 0
    for i in range(int(X-R), int(X+R)+1):
        for j in range(int(Y-R), int(Y+R)+1):
            if (i-X)**2 + (j-Y)**2 <= R**2:
                count += 1
    print(count)
    
    return

=======
Suggestion 10

def main():
    # put your code here
    print('Hello World!')
