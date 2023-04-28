Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, r = map(float, input().split())
    x = int(x * 10 ** 4)
    y = int(y * 10 ** 4)
    r = int(r * 10 ** 4)
    ans = 0
    for i in range(x - r, x + r + 1):
        d = (r ** 2 - (i - x) ** 2) ** 0.5
        u = y + d
        l = y - d
        if u % 10000 == 0:
            u -= 1
        if l % 10000 == 0:
            l += 1
        ans += (u // 10000 - l // 10000) + 1
    print(ans)

=======
Suggestion 2

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for y in range(Y - R, Y + R + 1):
        if (R ** 2 - (y - Y) ** 2) >= 0:
            x = int((R ** 2 - (y - Y) ** 2) ** 0.5)
            ans += int((X + x) / 10000) - int((X - x - 1) / 10000)
    print(ans)

=======
Suggestion 3

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for i in range(X-R, X+R+1):
        d = R * R - (X-i) * (X-i)
        if d >= 0:
            dy = int(d**0.5)
            ans += (Y + dy) // 10000 - (Y - dy) // 10000 + 1
    print(ans)

=======
Suggestion 4

def main():
    X, Y, R = map(float, input().split())

    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)

    ans = 0

    for x in range(X - R, X + R + 1):
        if x < 0:
            continue
        if x > 2 * X:
            break
        y = (R ** 2 - (x - X) ** 2) ** 0.5
        y1 = int(y + Y)
        y2 = int(Y - y)

        ans += y1 // 10000 - y2 // 10000 + 1

    print(ans)

=======
Suggestion 5

def main():
    import math
    x, y, r = map(float, input().split())
    x = math.floor(x*10000)
    y = math.floor(y*10000)
    r = math.floor(r*10000)
    count = 0
    for i in range(x-r, x+r+1):
        j = math.floor(math.sqrt(r**2 - (i-x)**2))
        count += math.floor((y+j)/10000) - math.floor((y-j)/10000) + 1
    print(count)

=======
Suggestion 6

def main():
    import math
    x, y, r = map(float, input().split())
    x = x * 10000
    y = y * 10000
    r = r * 10000
    x = round(x)
    y = round(y)
    r = round(r)
    ans = 0
    for i in range(-100000, 100001):
        if x - r > i * 10000:
            continue
        if x + r < i * 10000:
            break
        tmp = math.sqrt(r ** 2 - (i * 10000 - x) ** 2)
        ans += int((y + tmp) / 10000) - int((y - tmp) / 10000) + 1
    print(ans)

=======
Suggestion 7

def main():
    from decimal import Decimal
    import math
    x, y, r = map(Decimal, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    ans = 0
    for i in range(x - r, x + r + 1):
        if i < 0:
            continue
        if i > 100000 * 10000:
            break
        y2 = r * r - (x - i) * (x - i)
        if y2 < 0:
            continue
        y2 = int(math.sqrt(y2))
        if y2 < 0:
            continue
        y1 = y - y2
        y2 = y + y2
        y1 = (y1 + 9999) // 10000
        y2 = y2 // 10000
        ans += y2 - y1 + 1
    print(ans)

=======
Suggestion 8

def main():
    import math
    import sys
    input = sys.stdin.readline
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    ans = 0
    for i in range(x-r,x+r+1):
        if (r**2-(x-i)**2)**0.5%1 == 0:
            ans += 1
    for i in range(y-r,y+r+1):
        if (r**2-(y-i)**2)**0.5%1 == 0:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    x, y, r = map(float, input().split())
    x, y = int(x*10000), int(y*10000)
    r = int(r*10000)
    #print(x,y,r)
    ans = 0
    for i in range(-r, r+1):
        if i*i > r*r:
            break
        j = int((r*r-i*i)**0.5)
        #print(i,j)
        while i*i+j*j > r*r:
            j -= 1
        ans += (y+j)//10000 - (y+i-1)//10000
        ans += (y-i)//10000 - (y-j-1)//10000
    print(ans)

=======
Suggestion 10

def main():
    import math
    x, y, r = map(float, input().split())
    x, y = x*10000, y*10000
    r = r*10000
    x1 = math.ceil(x-r)
    x2 = math.floor(x+r)
    count = 0
    for i in range(x1, x2+1):
        y1 = math.ceil(y-math.sqrt(r**2-(x-i)**2))
        y2 = math.floor(y+math.sqrt(r**2-(x-i)**2))
        count += y2-y1+1
    print(count)
