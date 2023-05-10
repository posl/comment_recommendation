Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())

    x2 = (x0 + x1) / 2
    y2 = (y0 + y1) / 2

    x3 = x2 + y0 - y2
    y3 = y2 - x0 + x2

    print(x3, y3)

=======
Suggestion 2

def solve():
    import sys
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    if x0 == x1:
        print(x0, y1)
    else:
        a = (y1 - y0) / (x1 - x0)
        b = y0 - a * x0
        print((x0**2 + y0**2 - x1**2 - y1**2) / (2 * (x0 - x1)), a * (x0**2 - x1**2) / (2 * (x0 - x1)) + b)

=======
Suggestion 3

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN, yN = map(int, input().split())
    x1 = (x0+xN)/2 + (y0-yN)*3.0**0.5/2
    y1 = (y0+yN)/2 + (xN-x0)*3.0**0.5/2
    print(x1, y1)

=======
Suggestion 4

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    if y0 == y2:
        print(x1, y1)
    else:
        x3 = x1 + (x0 - x1) * ((y1 - y2) / (y0 - y2))
        y3 = y1 + (y0 - y1) * ((y1 - y2) / (y0 - y2))
        print(x3, y3)

=======
Suggestion 5

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = 0, 0
    x3, y3 = 0, 0
    if x0 == x1:
        x2 = x0 + abs(y0 - y1)
        x3 = x1 + abs(y0 - y1)
    elif y0 == y1:
        y2 = y0 + abs(x0 - x1)
        y3 = y1 + abs(x0 - x1)
    else:
        x2 = x0 + abs(y0 - y1)
        x3 = x1 + abs(y0 - y1)
        y2 = y0 + abs(x0 - x1)
        y3 = y1 + abs(x0 - x1)
    print(x2, y2)

=======
Suggestion 6

def main():
    import sys
    import math
    n = int(sys.stdin.readline())
    x0,y0 = map(int,sys.stdin.readline().split())
    x1,y1 = map(int,sys.stdin.readline().split())
    x2,y2 = map(int,sys.stdin.readline().split())
    x3,y3 = map(int,sys.stdin.readline().split())
    if x0 == x2:
        x4 = x1
    elif x0 == x1:
        x4 = x2
    else:
        x4 = x0
    if y0 == y2:
        y4 = y1
    elif y0 == y1:
        y4 = y2
    else:
        y4 = y0
    if x3 == x2:
        x5 = x1
    elif x3 == x1:
        x5 = x2
    else:
        x5 = x3
    if y3 == y2:
        y5 = y1
    elif y3 == y1:
        y5 = y2
    else:
        y5 = y3
    if x4 == x5:
        if x4 == x0:
            x1 = x2
        else:
            x1 = x0
        if y4 == y0:
            y1 = y2
        else:
            y1 = y0
    else:
        if x4 == x0:
            x1 = x5
        else:
            x1 = x4
        if y4 == y0:
            y1 = y5
        else:
            y1 = y4
    print(x1,y1)
main()

=======
Suggestion 7

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xh, yh = map(int, input().split())

    x1 = (x0 + xh + (yh - y0) * (3 ** 0.5)) / 2
    y1 = (y0 + yh + (x0 - xh) * (3 ** 0.5)) / 2
    print(x1, y1)

=======
Suggestion 8

def solve():
    # -*- coding: utf-8 -*-
    import math
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2 + math.sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2)) / 2
    y1 = (y0 + y2 + math.sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2)) / 2
    print(x1, y1)

=======
Suggestion 9

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())

    x2 = (x0 + x1 + (y0 - y1) * 2 ** 0.5) / 2
    y2 = (y0 + y1 + (x1 - x0) * 2 ** 0.5) / 2

    print(x2, y2)

=======
Suggestion 10

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2) / 2
    y1 = (y0 + yN2) / 2
    x2 = (x0 - xN2) / 2
    y2 = (y0 - yN2) / 2
    x3 = (y2 - y1) * (-1) + x1
    y3 = (x1 - x2) + y1
    print(x3, y3)
