Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    ans = 0
    for i in range(-r, r + 1):
        j = r - abs(i)
        if x - r <= i <= x + r:
            ans += (y + j + 9999) // 10000 - (y - j) // 10000 + 1
    print(ans)

=======
Suggestion 2

def main():
    import math
    x, y, r = map(float, input().split())
    x = int(x * 10**4)
    y = int(y * 10**4)
    r = int(r * 10**4)
    ans = 0
    for i in range(x - r, x + r + 1):
        if i % 10**4 != 0:
            continue
        y_range = r**2 - (i - x)**2
        y_range = math.floor(math.sqrt(y_range))
        y_min = y - y_range
        y_max = y + y_range
        y_min = math.ceil(y_min / 10**4) * 10**4
        y_max = math.floor(y_max / 10**4) * 10**4
        ans += (y_max - y_min) // 10**4 + 1
    print(ans)

=======
Suggestion 3

def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    x1 = x - r
    x2 = x + r
    ans = 0
    for i in range(x1, x2 + 1):
        y1 = y - r
        y2 = y + r
        for j in range(y1, y2 + 1):
            if (x - i) ** 2 + (y - j) ** 2 <= r ** 2:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    X,Y,R = map(float,input().split())
    X = int(X*10000)
    Y = int(Y*10000)
    R = int(R*10000)
    ans = 0
    for i in range(X-R,X+R+1):
        if (R**2-(i-X)**2)**0.5 == int((R**2-(i-X)**2)**0.5):
            ans += int((R**2-(i-X)**2)**0.5)//10000*2+1
        else:
            ans += int((R**2-(i-X)**2)**0.5)//10000*2
    print(ans)

=======
Suggestion 5

def main():
    import math
    x,y,r = map(float, input().split())
    x1 = math.ceil(x-r)
    x2 = math.floor(x+r)
    ans = 0
    for i in range(x1,x2+1):
        y1 = math.ceil(y - math.sqrt(r**2 - (x-i)**2))
        y2 = math.floor(y + math.sqrt(r**2 - (x-i)**2))
        ans += y2 - y1 + 1
    print(ans)
main()

=======
Suggestion 6

def main():
    # input
    X, Y, R = map(float, input().split())

    # compute
    ans = 0
    for i in range(int(X-R), int(X+R+1)):
        for j in range(int(Y-R), int(Y+R+1)):
            if (i-X)**2 + (j-Y)**2 <= R**2:
                ans += 1

    # output
    print(ans)

=======
Suggestion 7

def main():
    import math
    X, Y, R = map(float, input().split())
    ans = 0
    for i in range(math.ceil(X-R), math.floor(X+R)+1):
        if (R**2 - (X-i)**2)**0.5 % 1 == 0:
            ans += math.floor(Y + (R**2 - (X-i)**2)**0.5) - math.ceil(Y - (R**2 - (X-i)**2)**0.5) + 1
        elif (R**2 - (X-i)**2)**0.5 > 0:
            ans += math.floor(Y + (R**2 - (X-i)**2)**0.5) - math.ceil(Y - (R**2 - (X-i)**2)**0.5)
    print(ans)

=======
Suggestion 8

def main():
    import sys
    import math
    from decimal import Decimal
    input = sys.stdin.readline
    X, Y, R = map(Decimal, input().split())
    X = round(X * 10000)
    Y = round(Y * 10000)
    R = round(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1, 10000):
        if (R ** 2 - (x - X) ** 2).sqrt() % 10000 == 0:
            ans += 1
    ans *= 2
    for y in range(Y - R, Y + R + 1, 10000):
        if (R ** 2 - (y - Y) ** 2).sqrt() % 10000 == 0:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    #print("Hello World!")
    #print("Hello", "World!")
    #print("Hello" + "World!")
    #print("Hello" + " " + "World!")
    #print("Hello" + " " + "World!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!" + "!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!" + "!" + "!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!" + "!" + "!" + "!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!" + "!" + "!" + "!" + "!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!" + "!" + "!" + "!" + "!" + "!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!" + "!" + "!" + "!" + "!" + "!" + "!" + "!")
    #print("Hello" + " " + "World!" + "!" + "!" + "!" + "!" + "!" + "!" + "!
